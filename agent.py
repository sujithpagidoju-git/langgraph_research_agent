"""
Agent configuration and state management.
The agent uses LLM to decide which tools to use.
"""

from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from tools import TOOLS
from dotenv import load_dotenv
import os

load_dotenv()

class AgentState(TypedDict):
    """
    State represents the data that flows through our graph.
    messages: conversation history
    """
    messages: Annotated[Sequence[BaseMessage], add_messages]

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Bind tools
llm_with_tools = llm.bind_tools(TOOLS)

def call_model(state: AgentState) -> dict:
    """Call the LLM with tools."""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state: AgentState) -> str:
    """Decide whether to execute tools or finish."""
    messages = state["messages"]
    last_message = messages[-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"
