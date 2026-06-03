# from security.secure_retrieval import filter_authorized_docs

# retrieved_docs = [
#     {
#         "source": "employees.csv",
#         "access_level": "hr",
#         "content": "Alice Finance 120000"
#     },
#     {
#         "source": "sales.csv",
#         "access_level": "finance",
#         "content": "USA revenue 300000"
#     },
#     {
#         "source": "public_policy.pdf",
#         "access_level": "public",
#         "content": "General company policy"
#     }
# ]

# user_role = "employee"

# authorized_docs = filter_authorized_docs(
#     retrieved_docs,
#     user_role
# )

# print("User Role:", user_role)
# print("\nAccessible Documents:")

# for doc in authorized_docs:
#     print(doc["source"])



from security.secure_retrieval import filter_authorized_docs

retrieved_docs = [
    {"source": "employees.csv", "access_level": "hr"},
    {"source": "sales.csv", "access_level": "finance"},
    {"source": "security.pdf", "access_level": "admin"},
    {"source": "policy.pdf", "access_level": "public"}
]

for role in ["employee", "hr", "finance", "admin"]:

    docs = filter_authorized_docs(
        retrieved_docs,
        role
    )

    print(f"\nRole = {role}")

    for doc in docs:
        print(doc["source"])