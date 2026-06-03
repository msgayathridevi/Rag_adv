from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


def chunk_documents(documents):

    chunks = []

    for doc in documents:

        split_docs = splitter.split_text(doc["content"])

        for idx, chunk in enumerate(split_docs):

            chunks.append(
                {
                    "content": chunk,
                    "chunk_id": idx,
                    "source": doc["source"],
                    "source_type": doc["source_type"]
                }
            )

    return chunks