# test_bm25.py

import pickle

from retrieval.bm25_retriever import (
    build_bm25,
    retrieve_bm25
)

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

build_bm25(chunks)

results = retrieve_bm25(
    "What is Alice department?"
)

for doc, score in results:
    print("\nScore:", round(score, 4))
    print("Source:", doc["source"])
    print(doc["content"])