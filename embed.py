# embed.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from ingest import load_dataset

model = SentenceTransformer("all-MiniLM-L6-v2")
chunks = load_dataset()

texts = [
    f"{c.section} - {c.title}: {c.content}"
    for c in chunks
]

embeddings = model.encode(texts, show_progress_bar=True)

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))


def search(query, k=3):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)
    return [chunks[i] for i in I[0]]
