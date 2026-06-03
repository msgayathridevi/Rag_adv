from vectordb.chroma_store import collection
from embeddings.embedder import get_embeddings


def retrieve(query, k=3):

    query_embedding = get_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results