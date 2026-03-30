from langchain_openai import ChatOpenAI


# ✅ Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)


def generate_answer(query, docs):
    try:
        # Combine retrieved documents into context
        context = "\n\n".join([doc.page_content for doc in docs])

        # 🔥 FINAL PROMPT (structured + code-aware)
        prompt = f"""
You are a senior software engineer analyzing a codebase.

Give a clean, structured answer in this format:

## Overview
Explain what the project does in 2-3 sentences.

## Key Components
List and explain the main components.

## How It Works
Explain the internal flow step-by-step.

## Code References
Mention specific files, modules, or functions from the context if available.

## Summary
Give a short final summary.

Be precise, technical, and grounded ONLY in the provided context.
Do NOT hallucinate.

Context:
{context}

Question:
{query}
"""

        # Call LLM
        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
        return f"Error generating answer: {str(e)}"