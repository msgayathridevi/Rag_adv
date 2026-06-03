from retrieval.vector_retriever import retrieve

# query = "How many annual leave days are provided?"
# query = "Is MFA mandatory?"
# query = "What is Alice's department?"
# query = "Which server has high CPU usage?"
query = "What is the revenue in USA?"

results = retrieve(query)

print(results)