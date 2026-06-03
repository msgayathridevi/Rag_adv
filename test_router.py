# test_router.py

from retrieval.query_router import route_query

queries = [
    "How many leave days?",
    "What is Alice salary?",
    "What is revenue in USA?",
    "Any CPU alerts?",
    "Is MFA mandatory?"
]

for q in queries:
    print(q)
    print("->", route_query(q))
    print()