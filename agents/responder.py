def suggest_reply_agent(state):
    if state["category"] == "Finance":
        state["reply"] = "Thank you for the invoice. We'll process it soon."
    elif state["category"] == "Hiring":
        state["reply"] = "Thanks for your application. We'll review it and get back to you."
    else:
        state["reply"] = "Thanks for your message."
    return state
