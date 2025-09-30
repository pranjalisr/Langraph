LangGraph Project

LangGraph is a framework for building stateful, multi-step applications with LLMs.
It lets you define your app as a graph of nodes (functions, models, tools, APIs), where edges control how state flows between them.

🚀 Features

Graph-based orchestration: Define workflows with nodes & edges.

State management: Pass state between nodes easily.

LLM integration: Plug in OpenAI, Anthropic, or custom models.

Checkpoints: Persist state with backends like MongoDB or SQLite.

Streaming: Stream intermediate results from nodes.

📦 Installation
pip install langgraph

Optionally install integrations:

pip install langgraph[all]       (includes MongoDB, SQLAlchemy, Redis, etc.)

