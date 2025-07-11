from langchain_google_genai import ChatGoogleGenerativeAI
from config.env import GOOGLE_MODEL

llm = ChatGoogleGenerativeAI(model=GOOGLE_MODEL)

def summarize_agent(state):
    print("Summarizing email...", state)
    prompt = f"Summarize this email:\n\n{state['content']}"
    summary = llm.invoke(prompt)
    state["summary"] = summary.content
    return state
