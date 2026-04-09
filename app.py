from fastapi import FastAPI
from ingestion.load_structured_data import process_data
from agents.rag_agent import rag_agent
from agents.smart_data_agent import smart_data_agent
from agents.smart_router import smart_route

app = FastAPI()

# Load data once
df = process_data("data/structured/retail_store_inventory.csv")


@app.get("/")
def home():
    return {"message": "Supply Chain AI Assistant API running 🚀"}


@app.get("/query")
def query_api(q: str):
    agent_type = smart_route(q)

    if agent_type == "data":
        answer = smart_data_agent(q, df)
    else:
        # You may need to initialize DB once properly
        answer = rag_agent(q, None)

    return {"query": q, "answer": str(answer)}
