from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset

def evaluate_rag(query, answer, context):
    data = {
        "question": [query],
        "answer": [answer],
        "contexts": [context],
        "ground_truth": [answer]
    }

    dataset = Dataset.from_dict(data)

    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
    )

    print("\n📊 Evaluation Scores:")
    print(result)

    return result