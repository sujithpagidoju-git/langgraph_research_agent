"""
LangGraph workflow definition.
Creates the graph structure of our agent.
"""

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from agent import AgentState, call_model, should_continue
from tools import TOOLS

def create_graph():
    """Create the agent graph."""
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(TOOLS))

    # Entry point
    workflow.set_entry_point("agent")

    # Conditional edges
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )

    # Tool → Agent feedback loop
    workflow.add_edge("tools", "agent")

    # Compile graph
    app = workflow.compile()
    return app


def print_graph_structure():
    """Print ASCII graph structure."""
    print("""
====================
Graph Structure:

START
  ↓
[ AGENT ] (LLM decides)
  ↓
  ↳ [Decision Point]
      ↓
    [ TOOLS ] (Execute tools)
      ↓
      ↳ (back to AGENT)
  ↓
[END] Final Response
""")
