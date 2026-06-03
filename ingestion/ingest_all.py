from pdf_loader import load_pdfs
from csv_loader import load_csvs
from json_loader import load_jsons
from chunker import chunk_documents

from metadata_enricher import enrich_chunks

pdf_docs = load_pdfs()

csv_docs = load_csvs()

json_docs = load_jsons()

all_docs = pdf_docs + csv_docs + json_docs

# chunks = chunk_documents(all_docs)
chunks = chunk_documents(all_docs)

chunks = enrich_chunks(chunks)

print(f"Documents Loaded: {len(all_docs)}")
print(f"Chunks Created: {len(chunks)}")

for chunk in chunks[:5]:
    print("\n----------------")
    print(chunk)