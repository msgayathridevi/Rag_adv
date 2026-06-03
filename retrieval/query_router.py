def route_query(query):

    query = query.lower()

    hr_keywords = {
        "leave",
        "employee",
        "salary",
        "department",
        "vacation",
        "hr"
    }

    finance_keywords = {
        "sales",
        "revenue",
        "finance",
        "profit"
    }

    infra_keywords = {
        "server",
        "cpu",
        "latency",
        "alert",
        "infrastructure"
    }

    security_keywords = {
        "mfa",
        "password",
        "security",
        "access"
    }

    for word in hr_keywords:
        if word in query:
            return "hr"

    for word in finance_keywords:
        if word in query:
            return "finance"

    for word in infra_keywords:
        if word in query:
            return "admin"

    for word in security_keywords:
        if word in query:
            return "admin"

    return "all"