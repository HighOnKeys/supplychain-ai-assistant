import re
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



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

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text.strip()

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()
