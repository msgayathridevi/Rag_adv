def build_citations(docs):

    sources = []

    for doc in docs:

        source = doc["source"]

        if source not in sources:
            sources.append(source)

    return sources