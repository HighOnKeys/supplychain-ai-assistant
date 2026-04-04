from rag.rag_pipeline import retrieve_documents
from rag.llm_pipeline import generate_answer


def rag_agent(query, db):
    docs = retrieve_documents(query, db)
    answer = generate_answer(query, docs)
    return answer
