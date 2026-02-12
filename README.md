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

## Tech Stack
- Python
- SentenceTransformers / FAISS (or Chroma)
- Gemini / OpenAI (LLM)

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A Google API key for Gemini (set as `GOOGLE_API_KEY` environment variable)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/frenemy17/cold-case-rag-project.git
   cd cold-case-rag-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Required packages:
   - `faiss-cpu` or `faiss-gpu`
   - `sentence-transformers`
   - `google-genai`
   - `numpy`

4. **Set up environment variables:**
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

5. **Prepare evidence data:**
   - Add your evidence files (`.txt`) to the `data/` directory
   - Format: Use `# Section Name` for sections and `## Title` for subsections
   - Example structure:
     ```
     # Crime Scene Investigation
     ## Initial Report
     Evidence details here...
     
     ## Forensic Analysis
     More evidence details...
     ```

### Running the Project

1. **Embed the evidence:**
   ```bash
   python embed.py
   ```
   This creates vector embeddings of all evidence chunks.

2. **Query the system:**
   ```bash
   python main.py
   ```
   Or use the RAG module directly:
   ```python
   from rag import ask_rag
   answer = ask_rag("What evidence supports X?")
   print(answer)
   ```

## Why this project
Demonstrates:
- RAG fundamentals
- Hallucination control
- Source grounding
- Real-world AI system design
