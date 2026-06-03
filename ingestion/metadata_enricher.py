from pathlib import Path


def assign_access(source):

    source = source.lower()

    if "hr" in source:
        return "hr"

    elif "employee" in source:
        return "hr"

    elif "sales" in source:
        return "finance"

    elif "security" in source:
        return "admin"

    elif "infrastructure" in source:
        return "admin"

    elif "alert" in source:
        return "admin"

    else:
        return "public"


def enrich_chunks(chunks):

    enriched = []

    for chunk in chunks:

        chunk["access_level"] = assign_access(
            chunk["source"]
        )

        enriched.append(chunk)

    return enriched