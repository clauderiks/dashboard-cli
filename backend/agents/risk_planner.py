from typing import Dict, Any, List, Optional
from .llm_client import ollama_client
import json

class RiskPlanner:
    """Agent specialized in planning and task decomposition"""
    
    def decompose_task(self, task: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Break down a complex task into subtasks"""
        prompt = f"""Decompose this task into detailed, actionable subtasks:

Task: {task}
{f'Context: {context}' if context else ''}

Respond as JSON:
{{
    "main_task": "task",
    "subtasks": [
        {{
            "id": 1,
            "title": "subtask title",
            "description": "what needs to be done",
            "depends_on": [0],
            "estimated_time": "minutes"
        }}
    ],
    "total_estimated_time": "total minutes",
    "dependencies": "dependency notes"
}}
"""
        
        response = ollama_client.generate(prompt, temperature=0.5)
        
        if response["success"]:
            try:
                return json.loads(response["content"])
            except:
                return {"main_task": task, "subtasks": [{"title": task}]}
        return {"error": response["error"]}
    
    def prioritize_tasks(self, tasks: List[str], criteria: Optional[str] = None) -> Dict[str, Any]:
        """Prioritize a list of tasks"""
        tasks_str = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        
        prompt = f"""Prioritize these tasks {f'based on: {criteria}' if criteria else ''}:

{tasks_str}

Respond as JSON:
{{
    "prioritized": [
        {{
            "rank": 1,
            "task": "task",
            "priority": "high/medium/low",
            "reason": "why this priority"
        }}
    ],
    "critical_path": ["task1", "task2"],
    "notes": "additional notes"
}}
"""
        
        response = ollama_client.generate(prompt, temperature=0.5)
        
        if response["success"]:
            try:
                return json.loads(response["content"])
            except:
                return {"prioritized": [{"task": t} for t in tasks]}
        return {"error": response["error"]}
