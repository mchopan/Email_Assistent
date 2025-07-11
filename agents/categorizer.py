def categorize_agent(state):
    content = state["summary"]
    if "invoice" in content.lower():
        category = "Finance"
    elif "interview" in content.lower():
        category = "Hiring"
    else:
        category = "General"
    state["category"] = category
    return state
