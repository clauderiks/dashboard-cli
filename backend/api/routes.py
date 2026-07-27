from fastapi import APIRouter, HTTPException  
from typing import Optional  
import re  
import uuid  
from datetime import datetime  
  
from models import ChatRequest, ChatResponse  
from memory import memory  
from agents import RiskAgent, RiskCoder, RiskPlanner, ollama_client  
from tools import FileTools, TerminalTools, github_tools  
from config.settings import settings  
  
router = APIRouter(prefix="/api", tags=["chat"])  
  
risk_agent = RiskAgent()  
risk_coder = RiskCoder()  
risk_planner = RiskPlanner()  
  
  
def extract_command(message: str) -> Optional[str]:  
    """
    Extracts a shell command from a chat message.
    
    Parameters:
    	message (str): The chat message containing a fenced Bash or shell command, or a command prefixed with `!`.
    
    Returns:
    	str or None: The extracted command, or `None` when the message contains no supported command format.
    """  
    text = message.strip()  
  
    fence = re.search(r"```(?:bash|sh)\s*\n(.*?)```", text, re.DOTALL)  
    if fence:  
        return fence.group(1).strip()  
  
    if text.startswith("!"):  
        return text[1:].strip()  
  
    return None  
  
  
@router.post("/chat", response_model=ChatResponse)  
async def chat(request: ChatRequest):  
    """
    Process a chat message using the language model or an optionally enabled terminal tool.
    
    Terminal commands are executed when tool use is enabled and the message contains a supported command pattern. Otherwise, the message is sent to the language model.
    
    Returns:
        ChatResponse: The assistant response and any terminal tool invocation details.
    
    Raises:
        HTTPException: If processing or response generation fails.
    """  
    try:  
        memory.create_conversation(request.conversation_id, title=None)  
        memory.add_message(request.conversation_id, "user", request.message)  
  
        if request.use_tools:  
            command = extract_command(request.message)  
            if command:  
                if not settings.enable_terminal_tool:  
                    denied = (  
                        "Terminal tool dang bi tat. Dat ENABLE_TERMINAL_TOOL=true "  
                        "trong backend/.env de cho phep chay lenh."  
                    )  
                    memory.add_message(request.conversation_id, "assistant", denied)  
                    return ChatResponse(  
                        conversation_id=request.conversation_id,  
                        message=denied,  
                        tool_calls=[],  
                        timestamp=datetime.now(),  
                        model=ollama_client.model,  
                    )  
  
                result = TerminalTools.execute_command(command, timeout=30, sandbox=True)  
                output = (  
                    f"$ {command}\n"  
                    f"[exit code: {result['returncode']}]\n\n"  
                    f"--- stdout ---\n{result['stdout']}\n"  
                    f"--- stderr ---\n{result['stderr']}"  
                )  
                memory.add_message(request.conversation_id, "assistant", output)  
                return ChatResponse(  
                    conversation_id=request.conversation_id,  
                    message=output,  
                    tool_calls=[{"tool": "terminal", "command": command, "result": result}],  
                    timestamp=datetime.now(),  
                    model=ollama_client.model,  
                )  
  
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
    """
    Retrieve the messages for a conversation.
    
    Parameters:
        conversation_id (str): Identifier of the conversation.
    
    Returns:
        dict: An object containing the conversation identifier and its messages.
    """  
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
    """
    Create a conversation with a newly generated identifier.
    
    Parameters:
        conversation_id (str): Conversation identifier provided in the request path; it is not used.
    
    Returns:
        dict: The generated conversation identifier and a creation status.
    """  
    try:  
        conv_id = str(uuid.uuid4())  
        memory.create_conversation(conv_id)  
        return {"conversation_id": conv_id, "status": "created"}  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/tools/file/read")  
async def file_read(path: str):  
    """
    Read a file from the specified path.
    
    Parameters:
        path (str): Path to the file to read.
    
    Returns:
        The file-reading result.
    
    Raises:
        HTTPException: If the file cannot be read.
    """  
    try:  
        result = FileTools.read_file(path)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/tools/file/write")  
async def file_write(path: str, content: str):  
    """
    Write content to a file at the specified path.
    
    Parameters:
        path (str): Destination file path.
        content (str): Content to write.
    """  
    try:  
        result = FileTools.write_file(path, content)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/tools/terminal/execute")  
async def terminal_execute(command: str, timeout: int = 30, sandbox: bool = True):  
    """Execute a terminal command with the specified timeout and sandbox setting.
    
    Parameters:
        command (str): The terminal command to execute.
        timeout (int): Maximum execution time in seconds.
        sandbox (bool): Whether to run the command in a sandbox.
    
    Returns:
        The terminal command execution result.
    """  
    try:  
        result = TerminalTools.execute_command(command, timeout, sandbox)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.get("/tools/github/repo")  
async def github_get_repo(owner: str, repo: str):  
    """
    Retrieve information about a GitHub repository.
    
    Parameters:
        owner (str): GitHub repository owner.
        repo (str): GitHub repository name.
    
    Returns:
        The repository information.
    """  
    try:  
        result = github_tools.get_repo(owner, repo)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.get("/tools/github/issues")  
async def github_list_issues(owner: str, repo: str, state: str = "open"):  
    """
    List issues for a GitHub repository.
    
    Parameters:
        owner (str): GitHub repository owner.
        repo (str): Repository name.
        state (str): Issue state to list, such as ``"open"`` or ``"closed"``.
    
    Returns:
        The issues returned by GitHub.
    
    Raises:
        HTTPException: If the GitHub request fails.
    """  
    try:  
        result = github_tools.list_issues(owner, repo, state)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/agent/plan")  
async def agent_plan(task: str, context: Optional[str] = None):  
    """
    Generate an execution plan for a task.
    
    Parameters:
        task (str): Task for which to generate a plan.
        context (Optional[str]): Additional context to consider when planning.
    
    Returns:
        dict: The generated plan represented as a dictionary.
    """  
    try:  
        plan = risk_agent.plan(task, context)  
        return plan.dict()  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/coder/analyze")  
async def coder_analyze(code: str, language: str = "python"):  
    """Analyze source code in the specified programming language.
    
    Parameters:
        code (str): Source code to analyze.
        language (str): Programming language of the source code.
    
    Returns:
        The code analysis result.
    """  
    try:  
        result = risk_coder.analyze_code(code, language)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/coder/generate")  
async def coder_generate(description: str, language: str = "python"):  
    """Generate code based on a natural-language description.
    
    Parameters:
        description (str): Description of the code to generate.
        language (str): Programming language for the generated code.
    
    Returns:
        The generated code result.
    """  
    try:  
        result = risk_coder.generate_code(description, language)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.post("/planner/decompose")  
async def planner_decompose(task: str, context: Optional[str] = None):  
    """
    Decompose a task into actionable subtasks.
    
    Parameters:
    	task (str): The task to decompose.
    	context (Optional[str]): Additional context for task decomposition.
    
    Returns:
    	The resulting task decomposition.
    """  
    try:  
        result = risk_planner.decompose_task(task, context)  
        return result  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))  
  
@router.get("/health")  
async def health_check():  
    """Report the service health status and LLM connection details.
    
    Returns:
        dict: A health payload containing the status, timestamp, LLM model, and Ollama URL.
    """  
    return {  
        "status": "healthy",  
        "timestamp": datetime.now().isoformat(),  
        "llm_model": ollama_client.model,  
        "ollama_url": ollama_client.base_url  
    }  
