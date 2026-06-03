def confidence_score(retrieval_results):

    if not retrieval_results:
        return 0

    top_k = min(3, len(retrieval_results))

    score = 0.7 + (0.1 * top_k)

    return min(score, 1.0)