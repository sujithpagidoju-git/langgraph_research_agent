# 🚀 LangGraph Research Assistant Agent



A fully functional **AI Research Assistant** built using **LangGraph**, **LangChain**, and **OpenAI**.
This agent can:



* 🔎 Search the web
* 📝 Save findings to notes
* 🧮 Perform mathematical calculations
* 🤖 Decide when to use tools (ReAct style)
* 🔄 Follow a think → act → observe loop
* 🧠 Maintain conversation context



This project is perfect for beginners exploring **AI Agents** and developers wanting a **practical LangGraph example**.



---



## 📁 Project Structure



```
langgraph_research_agent/
│── agent.py              # Agent model config + tool binding
│── tools.py              # Custom tool functions
│── graph.py              # LangGraph workflow construction
│── main.py               # Entry point (interactive CLI agent)
│── research_notes.txt    # Saved notes output
│── venv/                 # Local virtual environment (ignored)
│── .gitignore
└── README.md
```



---



## 🛠️ Setup Instructions



### 1️⃣ Create Virtual Environment



```bash
python -m venv venv
source venv/bin/activate             # Windows: venv\Scripts\activate
```



### 2️⃣ Install Requirements



```bash
pip install langgraph langchain langchain-openai tavily-python python-dotenv
```



### 3️⃣ Add API Keys



Create a `.env` file:



```
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```



---



## ▶️ Running the Agent (Interactive Mode)



```bash
python main.py
```



Example usage:



```
You: What is 25 + 48 + 100?
Agent: Result: 173
```



```
You: Search recent AI breakthroughs and save the findings
Agent: Using tool: search_web
Agent: Using tool: save_to_notes
Agent: Successfully saved to research notes!
```



---



## 🧰 Features & Tools



### 🔍 `search_web(query)`



Simulated web search (can be replaced with Tavily API).



### 📝 `save_to_notes(content)`



Appends findings to `research_notes.txt` with timestamp.



### 🧮 `calculate(expression)`



Performs safe mathematical evaluation.



---



## 🧠 LangGraph Workflow (Graph Structure)



```
START
  ↓
[ AGENT ] → decides whether a tool is needed
  ↓
  ↳ (if tool call) → [ TOOLS ] → back to AGENT
  ↓
END (final response)
```



---



## 🔧 File-by-File Overview



### ✔ `tools.py`



Contains custom tools decorated via `@tool`.



### ✔ `agent.py`



Defines:



* `AgentState`
* LLM configuration
* Tool binding
* Routing logic (`should_continue`)



### ✔ `graph.py`



Builds the LangGraph:



* Nodes
* Edges
* Tool loop
* Conditional transitions



### ✔ `main.py`



Interactive CLI agent:



* Prompts user
* Streams reasoning/actions
* Displays tool usage
* Handles errors



---



## 📌 Example Query (Programmatic)



```python
from graph import create_graph
from langchain_core.messages import HumanMessage



app = create_graph()



response = app.invoke({
    "messages": [HumanMessage(content="Calculate 15 * 23")]
})



print(response["messages"][-1].content)
```



---



## 🧪 Extension Ideas (Next Steps)



* Integrate real **Tavily search**
* Add memory using LangGraph checkpointers
* Add more tools (file reader, API caller, summarizer)
* Add multi-agent collaboration
* Add human approval nodes



---



## 🧑‍💻 Author



Built by **Sai Sujith** as an end-to-end demo of LangGraph agent workflows.



---



## ⭐ Support the Project



If you like this project, give it a **⭐ star on GitHub**!



---
