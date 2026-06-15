from dataclasses import dataclass


@dataclass(frozen=True)
class Example:
    text: str
    label: int


def load_toy_sarcasm_dataset() -> list[Example]:
    return [
        Example("Great, another meeting that could have been an email.", 1),
        Example("I really appreciate the clear deployment checklist.", 0),
        Example("Perfect, the server crashed right before the demo.", 1),
        Example("The model card explains the limitations well.", 0),
        Example("Amazing, my tests failed because I forgot to install dependencies.", 1),
        Example("The evaluation metrics improved after data cleaning.", 0),
    ]

