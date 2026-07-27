from typing import Dict, Any, Optional, List
from models import AgentPlan, ChatResponse
from .llm_client import ollama_client
from tools import FileTools, TerminalTools, github_tools
import json

class RiskAgent:
    """Main agent for coordinating tasks and tool usage"""
    
    def __init__(self):
        self.tools_map = {
            "file_read": FileTools.read_file,
            "file_write": FileTools.write_file,
            "file_delete": FileTools.delete_file,
            "file_list": FileTools.list_files,
            "terminal_execute": TerminalTools.execute_command,
            "github_get_repo": github_tools.get_repo,
            "github_list_issues": github_tools.list_issues,
            "github_create_issue": github_tools.create_issue,
        }
    
    def plan(self, task: str, context: Optional[str] = None) -> AgentPlan:
        """Create a plan for the task"""
        prompt = f"""You are a helpful AI assistant. Create a detailed step-by-step plan to accomplish this task:
        
Task: {task}

{f'Context: {context}' if context else ''}

Provide your response as JSON with this structure:
{{
    "steps": ["step 1", "step 2", ...],
    "reasoning": "explanation",
    "tools_needed": ["tool1", "tool2", ...]
}}

Tools available:
- file_read, file_write, file_delete, file_list
- terminal_execute
- github_get_repo, github_list_issues, github_create_issue
"""
        
        response = ollama_client.generate(prompt)
        
        if response["success"]:
            try:
                plan_data = json.loads(response["content"])
                return AgentPlan(**plan_data)
            except:
                return AgentPlan(
                    steps=[task],
                    reasoning="Unable to parse plan",
                    tools_needed=[]
                )
        else:
            return AgentPlan(
                steps=[task],
                reasoning="Error generating plan",
                tools_needed=[]
            )
    
    async def run(self, task: str, max_steps: int = 5) -> Dict[str, Any]:
        """Run agent autonomously on a task"""
        plan = self.plan(task)
        results = []
        
        for step_idx, step in enumerate(plan.steps[:max_steps]):
            results.append({
                "step": step,
                "status": "pending"
            })
        
        return {
            "task": task,
            "plan": plan.dict(),
            "results": results,
            "completed": len(results) > 0
        }
