ROLE_PERMISSIONS = {
    "admin": [
        "admin",
        "hr",
        "finance",
        "public"
    ],

    "hr": [
        "hr",
        "public"
    ],

    "finance": [
        "finance",
        "public"
    ],

    "employee": [
        "public"
    ]
}


def has_access(user_role, document_access_level):

    allowed_levels = ROLE_PERMISSIONS.get(
        user_role,
        []
    )

    return document_access_level in allowed_levels