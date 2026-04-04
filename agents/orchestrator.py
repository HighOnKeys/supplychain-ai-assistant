def route_query(query):
    query = query.lower()

    # Decide based on intent
    if any(word in query for word in ["revenue", "sales", "product", "region"]):
        return "data"

    else:
        return "rag"
