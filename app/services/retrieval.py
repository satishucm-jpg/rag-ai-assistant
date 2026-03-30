import os

VECTORSTORE = []

def create_vectorstore(chunks):
    global VECTORSTORE
    VECTORSTORE = chunks


def retrieve_docs(query):
    if not VECTORSTORE:
        return []

    # simple keyword search
    results = []
    for doc in VECTORSTORE:
        if query.lower() in doc.page_content.lower():
            results.append(doc)

    # fallback → return first few docs
    return results[:3] if results else VECTORSTORE[:3]