import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained(
    "google/flan-t5-base")


def clean_text(text):
    text = re.sub(r"\[\d+\]", "", text)   # remove citations
    text = re.sub(r"\s+", " ", text)      # fix spacing
    return text.strip()


def build_context(docs):
    cleaned = []

    for doc in docs:
        text = clean_text(doc.page_content)

        # take only meaningful part
        sentences = text.split(".")
        sentences = [s.strip() for s in sentences if len(s.strip()) > 40]

        cleaned.extend(sentences[:2])   # take top 2 sentences per doc

    return ". ".join(cleaned)


def generate_answer(query, retrieved_docs):
    context = build_context(retrieved_docs)

    prompt = f"""
Answer the question using the context.

Follow these rules:
- Do NOT copy sentences
- Combine multiple ideas
- Explain clearly like a human expert
- Give a complete answer

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt",
                       truncation=True, max_length=512)

    outputs = model.generate(
        **inputs,
        max_new_tokens=180,
        min_length=60,          # forces longer answer
        do_sample=True,
        temperature=0.7,
        repetition_penalty=1.2
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()
