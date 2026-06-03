from retrieval.hybrid_retriever import hybrid_retrieve

results = hybrid_retrieve(
    "What is Alice department?"
)

for r in results:

    print("\n----------------")
    print("Method:", r["method"])
    print("Source:", r["source"])