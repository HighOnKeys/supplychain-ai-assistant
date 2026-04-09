# 🚀 STREAMLIT APP
import os
from agents.smart_router import smart_route
from agents.smart_data_agent import smart_data_agent
from agents.rag_agent import rag_agent
from rag.rag_pipeline import (
    load_documents,
    split_documents,
    create_vectorstore
)
from ingestion.load_structured_data import process_data
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# IMPORT YOUR SYSTEM

# PAGE CONFIG
st.set_page_config(page_title="AI Supply Chain Assistant", layout="wide")

st.title("🧠 AI Supply Chain Assistant")
st.write("Ask anything about supply chain, inventory, or your dataset")
st.markdown("### 🔍 Example Queries")
st.markdown("""
- What is demand forecasting?
- Which region has highest sales?
- Average demand forecast by category
""")
# LOAD DATA (CACHE FOR SPEED)


@st.cache_data
def load_data():
    file_path = "data/structured/retail_store_inventory.csv"
    return process_data(file_path)


df = load_data()

# LOAD RAG DB (CACHE)


@st.cache_resource
def load_rag():
    if os.path.exists("faiss_index"):
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
        docs = load_documents("data/docs")
        chunks = split_documents(docs)
        db = create_vectorstore(chunks)
        db.save_local("faiss_index")

    return db


db = load_rag()

# USER INPUT
query = st.text_input("💬 Ask your question:")

if st.button("Ask"):

    if query:
        with st.spinner("Thinking... 🤔"):

            try:
                # ROUTE QUERY
                agent_type = smart_route(query)

                st.write(f"🔍 Routing to: **{agent_type.upper()} agent**")

                # EXECUTE AGENT
                if "data" in agent_type:
                    answer = smart_data_agent(query, df)
                else:
                    answer = rag_agent(query, db)

                # OUTPUT
                st.subheader("🧠 Answer:")
                st.write(answer)

            except Exception as e:
                st.error("Something went wrong!")
                st.text(str(e))
