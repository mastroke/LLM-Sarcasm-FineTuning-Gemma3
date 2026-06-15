from llm_finetuning_eval_lab.data import load_toy_sarcasm_dataset
from llm_finetuning_eval_lab.evaluate import run_evaluation
from llm_finetuning_eval_lab.metrics import classification_metrics


def test_dataset_has_both_classes() -> None:
    labels = {example.label for example in load_toy_sarcasm_dataset()}

    assert labels == {0, 1}


def test_metrics_are_computed() -> None:
    metrics = classification_metrics([1, 0, 1, 0], [1, 0, 0, 0])

    assert metrics.accuracy == 0.75
    assert metrics.precision == 1.0
    assert metrics.recall == 0.5


def test_evaluation_report_is_complete() -> None:
    report = run_evaluation()

    assert report["task"] == "sarcasm_classification"
    assert report["dataset_size"] > 0
    assert report["f1"] >= 0

