def analyze_intent(query: str):
    # Simple NLP simulation
    if "help" in query.lower():
        return "help_request", 0.95
    elif "refund" in query.lower():
        return "refund_request", 0.90
    return "unknown", 0.50
