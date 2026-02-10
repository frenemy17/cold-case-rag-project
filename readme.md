# Cold Case RAG – Evidence-Based Question Answering

A Retrieval Augmented Generation (RAG) system that answers
questions strictly from forensic evidence and provides
source citations.

## Features
- Hierarchical evidence ingestion (section + title)
- Local vector search (no LLM hallucinations)
- Safe logical inference
- Source-aware answers

## How it works
1. Evidence files are parsed into structured chunks
2. Chunks are embedded and stored in a vector index
3. Relevant chunks are retrieved for each query
4. An LLM answers using only retrieved evidence

.

## Tech Stack
- Python
- SentenceTransformers / FAISS (or Chroma)
- Gemini / OpenAI (LLM)

## Why this project
Demonstrates:
- RAG fundamentals
- Hallucination control
- Source grounding
- Real-world AI system design
