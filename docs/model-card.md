# Model Card

## Model

Keyword baseline for sarcasm classification.

## Intended Use

This baseline is used to verify that the evaluation workflow is wired correctly before GPU fine-tuning is added.

## Metrics

Run:

```bash
python -m llm_finetuning_eval_lab.evaluate
```

## Limitations

- This is not an LLM and should not be treated as production quality.
- Keyword approaches miss context and can overfit phrasing.
- The baseline exists to make CI deterministic.

## Planned Upgrade

- Add Gemma-family LoRA/QLoRA configuration.
- Add calibration and robustness checks.
- Publish evaluation artifacts with each release.

