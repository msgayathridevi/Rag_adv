import pickle

from retrieval.vector_retriever import retrieve
from retrieval.bm25_retriever import (
    build_bm25,
    retrieve_bm25
)

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

build_bm25(chunks)


def hybrid_retrieve(query, k=3):

    combined = []

    # VECTOR RESULTS
    vector_results = retrieve(query, k)

    docs = vector_results["documents"][0]
    metas = vector_results["metadatas"][0]

    for doc, meta in zip(docs, metas):

        combined.append({
            "method": "vector",
            "source": meta["source"],
            "content": doc
        })

    # BM25 RESULTS
    bm25_results = retrieve_bm25(query, k)

    for doc, score in bm25_results:

        combined.append({
            "method": "bm25",
            "source": doc["source"],
            "content": doc["content"],
            "score": float(score)
        })

    return combined