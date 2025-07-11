from agents.reader import read_email_agent
from agents.summarizer import summarize_agent
from agents.categorizer import categorize_agent
from agents.responder import suggest_reply_agent
from tools.email_tools import get_last_email, get_email_content
from tools.reply_tools import send_email
from langgraph.graph import StateGraph, START, END

from typing import TypedDict

class EmailState(TypedDict):
    email_id: str | None
    content: str | None
    summary: str | None
    category: str | None
    reply: str | None

builder = StateGraph(EmailState)

builder.add_node("Reader", read_email_agent)
builder.add_node("Summarizer", summarize_agent)
builder.add_node("Categorizer", categorize_agent)
builder.add_node("Responder", suggest_reply_agent)

builder.set_entry_point("Reader")
builder.add_edge("Reader", "Summarizer")
builder.add_edge("Summarizer", "Categorizer")
builder.add_edge("Categorizer", "Responder")
builder.add_edge("Responder", END)

graph = builder.compile()

response = graph.invoke({})

print(response["summary"])
