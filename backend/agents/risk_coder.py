from typing import Dict, Any, Optional
from .llm_client import ollama_client
import json

class RiskCoder:
    """Agent specialized in code analysis and generation"""
    
    def analyze_code(self, code: str, language: str = "python") -> Dict[str, Any]:
        """Analyze code and provide insights"""
        prompt = f"""Analyze this {language} code and provide:
1. What it does
2. Any issues or improvements
3. Performance considerations

Code:
```{language}
{code}
```

Respond as JSON:
{{
    "summary": "brief description",
    "issues": ["issue1", "issue2"],
    "improvements": ["improvement1"],
    "performance_notes": "notes"
}}
"""
        
        response = ollama_client.generate(prompt, temperature=0.5)
        
        if response["success"]:
            try:
                return json.loads(response["content"])
            except:
                return {"summary": response["content"]}
        return {"error": response["error"]}
    
    def generate_code(self, description: str, language: str = "python") -> Dict[str, Any]:
        """Generate code based on description"""
        prompt = f"""Generate {language} code for this requirement:
{description}

Provide clean, well-commented code. Respond as JSON:
{{
    "code": "code here",
    "explanation": "brief explanation",
    "dependencies": ["dep1", "dep2"]
}}
"""
        
        response = ollama_client.generate(prompt, temperature=0.7)
        
        if response["success"]:
            try:
                return json.loads(response["content"])
            except:
                return {"code": response["content"]}
        return {"error": response["error"]}
    
    def fix_code(self, code: str, error: str, language: str = "python") -> Dict[str, Any]:
        """Fix broken code"""
        prompt = f"""Fix this {language} code that has an error:

Error: {error}

Code:
```{language}
{code}
```

Respond as JSON:
{{
    "fixed_code": "corrected code",
    "explanation": "what was wrong and how it was fixed"
}}
"""
        
        response = ollama_client.generate(prompt, temperature=0.5)
        
        if response["success"]:
            try:
                return json.loads(response["content"])
            except:
                return {"fixed_code": response["content"]}
        return {"error": response["error"]}
