from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")


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

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=5,
        do_sample=False
    )

    decision = tokenizer.decode(
        outputs[0], skip_special_tokens=True).strip().upper()

    # SAFETY FIX
    if "DATA" in decision:
        return "data"
    else:
        return "rag"
