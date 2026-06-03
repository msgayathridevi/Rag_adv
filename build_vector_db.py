from ingestion.pdf_loader import load_pdfs
from ingestion.csv_loader import load_csvs
from ingestion.json_loader import load_jsons
from ingestion.chunker import chunk_documents
from ingestion.metadata_enricher import enrich_chunks

from embeddings.embedder import get_embeddings
from vectordb.chroma_store import collection


pdf_docs = load_pdfs()
csv_docs = load_csvs()
json_docs = load_jsons()

all_docs = pdf_docs + csv_docs + json_docs

chunks = chunk_documents(all_docs)
chunks = enrich_chunks(chunks)

texts = [
    chunk["content"]
    for chunk in chunks
]

embeddings = get_embeddings(texts)

collection.add(
    ids=[
        f"doc_{i}"
        for i in range(len(chunks))
    ],
    documents=texts,
    embeddings=embeddings,
    metadatas=[
        {
            "source": c["source"],
            "source_type": c["source_type"],
            "access_level": c["access_level"]
        }
        for c in chunks
    ]
)

print("Vector DB Created")
print("Chunks Stored:", len(chunks))

import pickle

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)