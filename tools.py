"""
Custom tools for our research agent.
Tools are functions the agent can call to perform actions.
"""

from langchain.tools import tool
from datetime import datetime

@tool
def search_web(query: str) -> str:
    """Search the web for information. Use this when you need current information or facts."""
    # In production integrate with Tavily API
    return f"Search results for '{query}': [Simulated results - integrate Tavily API here]"

@tool
def save_to_notes(content: str) -> str:
    """Save important information to research notes file."""
    try:
        with open("research_notes.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n\n--- Note saved at {timestamp} ---\n")
            f.write(content)
        return "Successfully saved to research notes!"
    except Exception as e:
        return f"Error saving notes: {str(e)}"

@tool
def calculate(expression: str) -> str:
    """Perform mathematical calculations. Use for any math operations."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"

# List of all available tools
TOOLS = [search_web, save_to_notes, calculate]
