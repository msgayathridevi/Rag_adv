from security.rbac import has_access


def filter_authorized_docs(
        docs,
        user_role
):

    authorized = []

    for doc in docs:

        access_level = doc.get(
            "access_level",
            "public"
        )

        if has_access(
            user_role,
            access_level
        ):
            authorized.append(doc)

    return authorized