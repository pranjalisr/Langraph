from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"

)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": ["Hi, This is a message from ChatBot Node"] }    

def samplenode(state: State):
    print("\n\nInside chatbot node", state)
    return { "messages": ["Sample message appended"] }


graph_builder = StateGraph(State)

# ✅ First add nodes with their functions
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# ✅ Then connect them with edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state =graph.invoke(State({"messages": ["Hi, My name is P"]}))
print("\n\nupdated_state", updated_state)



#(START) -> chatbot -> samplenode -> END

#state = {messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey"]) -> ["Hi, This is a message from ChatBot"]
# state = { "messages": ["Hey there", "Hi, This is a message from ChatBot"] }

