# rag.py
import numpy as np
from google import genai
from embed import search

SYSTEM_PROMPT = """
You are an investigative assistant.

You must answer questions using ONLY the provided evidence.
You are allowed to make logical inferences from the evidence,
but you must NOT invent new facts.

If the answer cannot be logically inferred from the evidence,
reply exactly: "Not enough evidence."

For every claim you make, cite the source file in brackets.
"""

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def build_context(chunks):
    context = ""
    for i, c in enumerate(chunks):
        cid = f"S{i+1}"
        context += f"[{cid}] {c.section} - {c.title}:\n{c.content}\n\n"
    return context


def ask_rag(question, k=3):
    retrieved = search(question, k)
    context = build_context(retrieved)

    final_prompt = f"""
EVIDENCE:
{context}

QUESTION:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + "\n\n" + final_prompt
    )

    return response.text
