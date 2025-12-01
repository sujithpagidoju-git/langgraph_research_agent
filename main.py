"""
Main entry point for the research assistant agent.
"""

from graph import create_graph, print_graph_structure
from langchain_core.messages import HumanMessage
import os

def run_agent():
    """Run the interactive research assistant."""
    print("=" * 60)
    print(" RESEARCH ASSISTANT AGENT (Powered by LangGraph)")
    print("=" * 60)

    print("\nCapabilities:")
    print(" • Web search for information")
    print(" • Save findings to notes")
    print(" • Perform calculations")

    print("\nCommands:")
    print(" • graph - Show graph structure")
    print(" • quit  - Exit")
    print("=" * 60)

    app = create_graph()

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue

            if user_input.lower() == "quit":
                print("\nGoodbye!")
                break

            if user_input.lower() == "graph":
                print_graph_structure()
                continue

            messages = [HumanMessage(content=user_input)]

            print("\nAgent thinking...\n")

            for event in app.stream({"messages": messages}):
                for value in event.values():
                    if "messages" in value:
                        last = value["messages"][-1]

                        if hasattr(last, "content") and last.content:
                            print(f"Agent: {last.content}")

                        if hasattr(last, "tool_calls") and last.tool_calls:
                            for tool_call in last.tool_calls:
                                print(f"Using tool: {tool_call['name']}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")


def run_example():
    """Run a simple example."""
    app = create_graph()
    query = "Search for the latest developments in AI agents and save the key findings to notes"
    print(f"\nQuery: {query}\n")
    messages = [HumanMessage(content=query)]

    for event in app.stream({"messages": messages}):
        for value in event.values():
            if "messages" in value:
                last = value["messages"][-1]
                print(last.content)


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found.")
        exit(1)

    run_agent()
    # run_example()
