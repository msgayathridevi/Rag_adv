from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

dataset = Dataset.from_dict({
    "question": [
        "How many leave days do employees receive?"
    ],
    "answer": [
        "Employees receive 20 annual leave days."
    ],
    "contexts": [[
        "Employees receive 20 annual leave days."
    ]],
    "ground_truth": [
        "Employees receive 20 annual leave days."
    ]
})

results = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall
    ]
)

print(results)