from langchain_core.tools import tool
from tools.email_tools import get_last_email, get_email_content

def read_email_agent(state):
    """Reads the last email and returns the content"""
    email_id = get_last_email()
    content = get_email_content(email_id)
    state["email_id"] = email_id
    state["content"] = content
    return state


