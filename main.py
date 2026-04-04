from agents.smart_router import smart_route
from agents.smart_data_agent import smart_data_agent
from agents.rag_agent import rag_agent
from rag.rag_pipeline import (
    load_documents,
    split_documents,
    create_vectorstore
)
from ingestion.load_structured_data import process_data
import os
from transformers import logging
import warnings
warnings.filterwarnings("ignore")

logging.set_verbosity_error()


# 📊 LOAD STRUCTURED DATA


file_path = "data/structured/retail_store_inventory.csv"
df = process_data(file_path)

print("\n✅ DATA PROCESSED SUCCESSFULLY\n")
print(df.head())
print("\nColumns:\n", df.columns)

# 📚 LOAD / CACHE RAG SYSTEM


# Check if FAISS index already exists
if os.path.exists("faiss_index"):
    print("\n⚡ Loading existing vector DB...\n")

    from langchain_community.vectorstores import FAISS
    from langchain_huggingface import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

else:
    print("\n🚀 Creating new vector DB...\n")

    docs = load_documents("data/docs")
    chunks = split_documents(docs)
    db = create_vectorstore(chunks)

    db.save_local("faiss_index")


# 💬 USER QUERY LOOP

while True:
    query = input("\n💬 Ask your question (or type 'exit'): ")

    if query.lower() == "exit":
        print("\n👋 Exiting system...")
        break

    try:
        # ROUTE QUERY
        agent_type = smart_route(query)

        print(f"\n🔍 Routing to: {agent_type.upper()} agent...\n")

        # EXECUTE AGENT
        if "data" in agent_type:
            answer = smart_data_agent(query, df)
        else:
            answer = rag_agent(query, db)

    except Exception as e:
        answer = "❌ Sorry, something went wrong while processing your query."
        print("ERROR:", e)

    # 🧠 OUTPUT

    print("\n" + "="*60)
    print("🧠 FINAL ANSWER:\n")
    print(answer)
    print("="*60)
