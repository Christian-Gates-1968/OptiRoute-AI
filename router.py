"""
OptiRoute AI - Intelligent Model Router
This module contains the core routing logic that decides which LLM to use based on prompt complexity.
"""

import os
from typing import Tuple
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ModelRouter:
    """
    Intelligent router that selects the optimal LLM based on prompt complexity.
    
    Philosophy: "High slope > high intercept" - optimize for speed and cost when possible,
    escalate to powerful models only when necessary.
    """
    
    def __init__(self):
        """Initialize both model providers with API keys from environment."""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        # Initialize the "Smart" model (GPT-4) - High quality, higher cost
        self.llm_smart = ChatOpenAI(
            model="gpt-4",
            api_key=self.openai_api_key,
            temperature=0.7
        )
        
        # Initialize the "Fast" model (Llama 3 via Groq) - Fast, low cost
        self.llm_fast = ChatGroq(
            model="llama3-8b-8192",
            api_key=self.groq_api_key,
            temperature=0.7
        )
        
        # Complexity thresholds (tunable based on use case)
        self.word_count_threshold = 15  # Queries with more words likely need reasoning
        self.reasoning_keywords = [
            "explain", "analyze", "compare", "evaluate", "why", "how does",
            "what is the difference", "reasoning", "elaborate", "justify"
        ]
    
    def analyze_complexity(self, prompt: str) -> dict:
        """
        Analyze the complexity of a user prompt.
        
        Args:
            prompt: The user's input query
            
        Returns:
            dict containing complexity score, reasoning, and model decision
        """
        word_count = len(prompt.split())
        prompt_lower = prompt.lower()
        
        # Check for reasoning keywords
        has_reasoning_keyword = any(
            keyword in prompt_lower for keyword in self.reasoning_keywords
        )
        
        # Determine complexity and model selection
        if has_reasoning_keyword or word_count > self.word_count_threshold:
            return {
                "complexity": "high",
                "word_count": word_count,
                "has_reasoning": has_reasoning_keyword,
                "model": "gpt-4",
                "provider": "openai",
                "reason": "Complex query detected - requires advanced reasoning",
                "icon": "🧠"
            }
        else:
            return {
                "complexity": "low",
                "word_count": word_count,
                "has_reasoning": has_reasoning_keyword,
                "model": "llama3-8b-8192",
                "provider": "groq",
                "reason": "Simple query - optimizing for speed and cost",
                "icon": "⚡"
            }
    
    def get_best_model(self, prompt: str) -> Tuple[object, str, dict]:
        """
        Select the best model for a given prompt.
        
        Args:
            prompt: The user's input query
            
        Returns:
            Tuple of (model_instance, model_display_name, analysis_details)
        """
        analysis = self.analyze_complexity(prompt)
        
        if analysis["provider"] == "openai":
            return (
                self.llm_smart,
                f"{analysis['icon']} GPT-4 (Smart Model)",
                analysis
            )
        else:
            return (
                self.llm_fast,
                f"{analysis['icon']} Llama 3 via Groq (Fast Model)",
                analysis
            )
    
    def get_response(self, prompt: str) -> dict:
        """
        Get a response from the optimal model.
        
        Args:
            prompt: The user's input query
            
        Returns:
            dict containing the response, model used, and routing analysis
        """
        model, model_name, analysis = self.get_best_model(prompt)
        
        try:
            response = model.invoke(prompt)
            return {
                "success": True,
                "response": response.content,
                "model": model_name,
                "analysis": analysis,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "response": None,
                "model": model_name,
                "analysis": analysis,
                "error": str(e)
            }
