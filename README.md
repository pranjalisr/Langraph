
# LangGraph Chatbot Workflows

A simple LangGraph-based project that demonstrates how to build LLM workflows using graph nodes, shared state, and conditional routing.

## Features

- Basic LangGraph chatbot flow
- State-based message handling
- Multiple graph nodes
- Conditional routing between nodes
- OpenAI `gpt-4.1-mini` integration
- `.env` support for API keys

## Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI API
- python-dotenv

## Project Structure

```bash
Langraph/
├── chat.py      # Basic LangGraph flow with chatbot and sample node
└── chat2.py     # Conditional graph flow with response evaluation
```

## How It Works
```
chat.py
```
This file creates a simple graph:
```

START → chatbot → samplenode → END
```

The graph takes an initial message, passes it through a chatbot node, appends another message through a sample node, and returns the updated state.
```
chat2.py
```
This file demonstrates a slightly more advanced workflow:
```

START → chatbot → evaluate_response → endnode → END
```
It sends the user query to an OpenAI model, stores the LLM response in state, and uses conditional routing to decide the next node.

## Setup

Clone the repository:
```
git clone https://github.com/pranjalisr/Langraph.git
cd Langraph/Lang/Langraph
```
Install dependencies:
```
pip install langgraph langchain openai python-dotenv typing-extensions
```
Create a .env file:

```
OPENAI_API_KEY=your_openai_api_key_here
```
# Run the Project

Run the basic graph:
```
python chat.py
```
Run the conditional graph:
```
python chat2.py
```
Example Query
```
updated_state = graph.invoke({
    "user_query": "Hey, What is 2+2?"
})
```
# What I Learned
- How LangGraph represents AI workflows as graphs
- How to define shared state using TypedDict
- How to add nodes and edges in a LangGraph workflow
- How to use conditional edges for routing
- How to connect OpenAI models with graph-based execution
- Future Improvements
- Add proper response quality evaluation
- Add Gemini or another fallback model
- Add memory support
Add streaming responses
Build a simple UI using Streamlit or FastAPI
Add error handling and logging
