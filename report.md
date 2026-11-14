# NimbusPay Ticket Triage — Assessment Report

**Candidate:** [Enter your name]  
**Role:** ML Intern – LLM Fine-Tuning, VIMA3YA  
**Base model:** `Qwen/Qwen2.5-1.5B-Instruct`  
**Method:** PEFT LoRA / QLoRA  
**Target hardware:** Google Colab free-tier NVIDIA T4

## A. Data audit and cleaning

The supplied training split contains 1,445 records. Twenty-five assistant targets are truncated or malformed JSON and were dropped because a complete target cannot be reconstructed safely. The remaining 1,420 records were retained. The cleaning pipeline reads only `train.jsonl` and applies the provided `SCHEMA.md` rules; development and test rows are never used to create training labels.

The audit identified 70 legacy `prio` fields with `low/medium/high` values, 30 non-ISO transaction dates, 20 noncanonical transaction IDs, 65 priority conflicts with the schema rules and four `needs_human` conflicts. These issue counts overlap. In total, 157 unique rows were fixed, producing 182 row-level cleaning-log entries; 25 rows were dropped. The complete `id,action,reason` log is in `cleaning_log.csv`.

Priority was recomputed in the documented order: fraud, disputed amount at least ₹50,000, or a legal threat gives P1; otherwise account access, or payment-failed/refund at least ₹5,000, gives P2; all remaining cases are P3. `needs_human` is true for P1 or explicit repeat-contact wording. Existing null transaction fields were not filled by guessing.

## B. Baselines

| Baseline | Dev exact match | Mean field accuracy | JSON valid |
|---|---:|---:|---:|
| Base model, fixed prompt | **[Fill from run]** | **[Fill]** | **[Fill]** |
| Base model, schema rules in prompt (reference only) | **[Fill from run]** | **[Fill]** | **[Fill]** |

The rule-augmented prompt is a reference baseline only. Fine-tuning and hidden-test inference use the original fixed system/user messages without schema rules in the prompt.

## C–D. Fine-tuning and controlled experiments

The selected model is `Qwen/Qwen2.5-1.5B-Instruct`, an instruction model below the 4B parameter limit. The notebook uses the model's chat template and masks system/user prompt tokens so loss is applied to assistant target tokens only. The sequence cap is selected from the 95th percentile of tokenized training examples. The starting LoRA configuration uses rank 8, alpha 16, dropout 0.05, a learning rate of 2e-4, three epochs, micro-batch size 2, gradient accumulation 8 and paged 8-bit AdamW. The notebook checks that trainable parameters remain below 50 million.

| Experiment | Controlled change | Dev exact match | Mean field accuracy | Peak GPU memory | Training minutes |
|---|---|---:|---:|---:|---:|
| E1a | Raw parseable labels, QLoRA rank 8 | **[Fill]** | **[Fill]** | **[Fill]** | **[Fill]** |
| E1b | Cleaned labels, QLoRA rank 8 | **[Fill]** | **[Fill]** | **[Fill]** | **[Fill]** |
| E2 | fp16 LoRA rank 8 vs E1b QLoRA | **[Fill]** | **[Fill]** | **[Fill]** | **[Fill]** |
| E3 | QLoRA rank 16 vs E1b rank 8 | **[Fill]** | **[Fill]** | **[Fill]** | **[Fill]** |
| E4 | Category-balanced vs ordinary sampling | **[Fill]** | **[Fill]** | **[Fill]** | **[Fill]** |

Do not submit this report with placeholders. Replace every value with measurements from `experiment_results.csv` and `report_results.json`; explain any failed run honestly.

## E. Error analysis

After the best model is selected, the notebook reports the weakest fields and categories and writes development-set failures to `dev_error_analysis_first10.csv`. Add at least ten specific explanations here based on actual model outputs. Discuss whether each failure relates to category confusion, priority thresholds/legal threats, amount extraction/conversion, date normalization, transaction-ID normalization, channel extraction, Hinglish detection or repeat-contact detection. Do not present hypothetical examples as observed failures.

## What I would do with one more week

1. Add train-only examples for rare categories and difficult Hinglish/date/amount patterns, with strict schema validation.
2. Add targeted adversarial cases for priority precedence and distracting non-transaction amounts.
3. Compare another model under 4B parameters and test learning-rate or epoch changes while controlling other settings.
4. Improve inference reliability through better training data and model selection, not output repair, constrained decoding or external APIs.

## AI tools used

ChatGPT assisted with interpreting the requirements, drafting/reviewing the data-cleaning and training notebook, and preparing the documentation structure. The notebook does not call an external LLM/API to create labels or predictions. All reported model results must come from the candidate's own Colab execution and must be reviewed and defended by the candidate.
