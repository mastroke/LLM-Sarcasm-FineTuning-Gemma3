from llm_finetuning_eval_lab.data import Example


SARCASM_MARKERS = {
    "great",
    "perfect",
    "amazing",
    "another",
    "crashed",
    "failed",
}


def predict(example: Example) -> int:
    tokens = set(example.text.lower().replace(",", "").replace(".", "").split())
    return int(bool(tokens.intersection(SARCASM_MARKERS)))

