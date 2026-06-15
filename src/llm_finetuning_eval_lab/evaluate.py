import json

from llm_finetuning_eval_lab.baseline import predict
from llm_finetuning_eval_lab.data import load_toy_sarcasm_dataset
from llm_finetuning_eval_lab.metrics import classification_metrics


def run_evaluation() -> dict:
    dataset = load_toy_sarcasm_dataset()
    y_true = [example.label for example in dataset]
    y_pred = [predict(example) for example in dataset]
    metrics = classification_metrics(y_true, y_pred)
    return {
        "task": "sarcasm_classification",
        "model": "keyword_baseline",
        "dataset_size": len(dataset),
        "accuracy": round(metrics.accuracy, 4),
        "precision": round(metrics.precision, 4),
        "recall": round(metrics.recall, 4),
        "f1": round(metrics.f1, 4),
    }


if __name__ == "__main__":
    print(json.dumps(run_evaluation(), indent=2))

