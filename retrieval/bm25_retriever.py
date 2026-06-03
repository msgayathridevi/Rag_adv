# retrieval/bm25_retriever.py

import re
from rank_bm25 import BM25Okapi

bm25 = None
documents = None

STOPWORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "of",
    "in",
    "to",
    "for",
    "and",
    "on",
    "at",
    "who",
    "which",
    "where",
    "when",
    "how",
    "does",
    "do",
    "are",
    "was",
    "were"
}


def tokenize(text):
    """
    Convert text into clean tokens.
    Example:
    'What is Alice department?'
    ->
    ['alice', 'department']
    """

    tokens = re.findall(r"\w+", text.lower())

    tokens = [
        token
        for token in tokens
        if token not in STOPWORDS
    ]

    return tokens


def build_bm25(chunks):
    """
    Build BM25 index from chunk documents.
    """

    global bm25
    global documents

    documents = chunks

    tokenized_docs = [
        tokenize(chunk["content"])
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_docs)

    print(f"BM25 index built for {len(chunks)} documents")


def retrieve_bm25(query, k=3):
    """
    Retrieve top-k documents using BM25.
    """

    global bm25
    global documents

    if bm25 is None:
        raise ValueError(
            "BM25 index not initialized. Call build_bm25() first."
        )

    query_tokens = tokenize(query)

    scores = bm25.get_scores(query_tokens)

    ranked_docs = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_docs[:k]