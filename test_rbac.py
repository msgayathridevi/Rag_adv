# test_rbac.py

from security.rbac import has_access

tests = [

    ("admin", "hr"),

    ("admin", "finance"),

    ("employee", "hr"),

    ("employee", "finance"),

    ("hr", "hr"),

    ("finance", "finance")
]

for role, level in tests:

    print(
        role,
        level,
        has_access(role, level)
    )