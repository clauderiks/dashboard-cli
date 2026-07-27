from fastapi import APIRouter, HTTPException
from typing import Optional
import uuid
from datetime import datetime

from models import ChatRequest, ChatResponse
from memory import memory
from agents import RiskAgent, RiskCoder, RiskPlanner, ollama_client
from tools import FileTools, TerminalTools, github_tools

router = APIRouter(prefix="/api", tags=["chat"])

risk_agent = RiskAgent()
risk_coder = RiskCoder()
risk_planner = RiskPlanner()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint - send message and get AI response"""
    try:
        memory.create_conversation(request.conversation_id, title=None)
        memory.add_message(request.conversation_id, "user", request.message)
        
        system_prompt = request.system_prompt or """You are Risk AI, a helpful coding assistant inspired by GitHub Copilot and OpenAI's Codex. 
You can read code, write code, execute commands, and interact with GitHub. 
Be concise and helpful."""
        
        response = ollama_client.generate(
            prompt=request.message,
            system=system_prompt,
            temperature=0.7,
            max_tokens=2048
        )
        
        if not response["success"]:
            raise HTTPException(status_code=500, detail=response["error"])
        
        memory.add_message(request.conversation_id, "assistant", response["content"])
        
        return ChatResponse(
            conversation_id=request.conversation_id,
            message=response["content"],
            tool_calls=[],
            timestamp=datetime.now(),
            model=ollama_client.model
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chat/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get conversation history"""
    try:
        messages = memory.get_messages(conversation_id)
        return {
            "conversation_id": conversation_id,
            "messages": messages
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/{conversation_id}/new")
async def new_conversation(conversation_id: str):
    """Create a new conversation"""
    try:
        conv_id = str(uuid.uuid4())
        memory.create_conversation(conv_id)
        return {"conversation_id": conv_id, "status": "created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tools/file/read")
async def file_read(path: str):
    """Read file contents"""
    try:
        result = FileTools.read_file(path)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tools/file/write")
async def file_write(path: str, content: str):
    """Write to file"""
    try:
        result = FileTools.write_file(path, content)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tools/terminal/execute")
async def terminal_execute(command: str, timeout: int = 30, sandbox: bool = True):
    """Execute terminal command"""
    try:
        result = TerminalTools.execute_command(command, timeout, sandbox)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tools/github/repo")
async def github_get_repo(owner: str, repo: str):
    """Get GitHub repository info"""
    try:
        result = github_tools.get_repo(owner, repo)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tools/github/issues")
async def github_list_issues(owner: str, repo: str, state: str = "open"):
    """List GitHub issues"""
    try:
        result = github_tools.list_issues(owner, repo, state)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/agent/plan")
async def agent_plan(task: str, context: Optional[str] = None):
    """Get agent plan for a task"""
    try:
        plan = risk_agent.plan(task, context)
        return plan.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/coder/analyze")
async def coder_analyze(code: str, language: str = "python"):
    """Analyze code"""
    try:
        result = risk_coder.analyze_code(code, language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/coder/generate")
async def coder_generate(description: str, language: str = "python"):
    """Generate code from description"""
    try:
        result = risk_coder.generate_code(description, language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/planner/decompose")
async def planner_decompose(task: str, context: Optional[str] = None):
    """Decompose task into subtasks"""
    try:
        result = risk_planner.decompose_task(task, context)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "llm_model": ollama_client.model,
        "ollama_url": ollama_client.base_url
    }
