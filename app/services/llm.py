def generate_answer(question: str, docs: list):
    context = "\n\n".join([doc.page_content for doc in docs])

    if not context:
        return "No relevant information found."

    return f"""
Answer based on repository:

{context[:1000]}

---
Question: {question}
"""