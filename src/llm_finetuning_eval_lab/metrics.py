from dataclasses import dataclass


@dataclass(frozen=True)
class Metrics:
    accuracy: float
    precision: float
    recall: float
    f1: float


def classification_metrics(y_true: list[int], y_pred: list[int]) -> Metrics:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have equal length")

    tp = sum(1 for truth, pred in zip(y_true, y_pred) if truth == pred == 1)
    fp = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 0 and pred == 1)
    fn = sum(1 for truth, pred in zip(y_true, y_pred) if truth == 1 and pred == 0)
    correct = sum(1 for truth, pred in zip(y_true, y_pred) if truth == pred)

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    return Metrics(
        accuracy=correct / len(y_true),
        precision=precision,
        recall=recall,
        f1=f1,
    )

