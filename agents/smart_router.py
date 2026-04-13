from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def smart_route(query):
    q = query.lower()

    # RULE BASED PRIORITY
    if any(word in q for word in ["revenue", "sales", "region", "product", "average", "sum"]):
        return "data"

    prompt = f"""
You are a classifier.

Classify the query into ONE category:

DATA → numerical, statistics, revenue, sales, dataset queries  
RAG → explanation, definition, theory, concept

Query: {query}

Answer ONLY one word: DATA or RAG
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",   # 🔥 IMPORTANT
        contents=prompt
    )

    output = response.text.strip()

    return output
    

    # SAFETY FIX
    if "DATA" in decision:
        return "data"
    else:
        return "rag"
