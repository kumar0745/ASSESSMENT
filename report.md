# NimbusPay Ticket Triage — Final Assessment Report

**Role:** ML Intern — LLM Fine-Tuning Assessment  
**Base model:** `Qwen/Qwen2.5-1.5B-Instruct`  
**Best run:** `E2_clean_lora_fp16_r8` (clean data, FP16 LoRA, rank 8, unbalanced sampling)  
**Runtime:** Google Colab NVIDIA Tesla T4 (driver 580.82.07, CUDA 13.0)

## 1. Data audit and cleaning

The supplied training split had **1,445** records. The audit retained **1,420** parseable training examples and dropped **25** examples with truncated or malformed assistant JSON. It repaired **157 unique rows** and recorded **182 actions** in `cleaning_log.csv` (157 fixes and 25 drops). Recorded fixes include 70 legacy `prio` field/value normalizations, 65 priority corrections, 30 date normalizations, 20 transaction-ID normalizations and 4 `needs_human` corrections. The dev split contains **200** rows and the held-out test split contains **400** rows. Dev/test data were used for evaluation/inference, not fine-tuning.

## 2. Baselines and controlled experiments

Baseline evaluation on 200 dev records: fixed-prompt baseline **0.0% exact match**, **0.0% mean field accuracy**, **0.0% JSON-valid**; rules-in-prompt reference baseline **0.5% exact match**, **8.6875% mean field accuracy**, **14.0% JSON-valid**.

| Run | Configuration | Dev exact match | Mean field accuracy | JSON valid | Peak GPU memory | Train time (min) |
|---|---|---:|---:|---:|---:|---:|
| E1 raw QLoRA r8 | Raw data, 4-bit, r=8 | 74.50% | 95.6875% | 100%* | 3.004 GB | 23.56 |
| E1 clean QLoRA r8 | Clean data, 4-bit, r=8 | 83.50% | 97.1875% | 100%* | 3.003 GB | 23.89 |
| E2 clean LoRA FP16 r8 | Clean data, FP16, r=8 | **86.50%** | **97.3750%** | **100%** | 3.899 GB | **18.15** |
| E3 clean QLoRA r16 | Clean data, 4-bit, r=16 | 81.50% | 96.8125% | 100%* | 3.066 GB | 24.30 |
| E4 clean balanced QLoRA r8 | Clean data, 4-bit, r=8, balanced sampling | 78.50% | 96.0625% | 100%* | 3.003 GB | 24.43 |

`E2_clean_lora_fp16_r8` was selected by dev exact match, then mean field accuracy, then JSON validity. It achieved **173/200 exact matches** and 97.375% mean per-field accuracy with 100% JSON-valid outputs. It was loaded in FP16, **not 4-bit**. QLoRA runs were 4-bit. The raw-vs-clean comparison improved exact match by 9.0 percentage points; the rank-16 variant did not beat rank 8; balanced sampling did not improve the clean-data r8 result. `*` JSON-valid was 100% for the evaluated runs per the run metrics/report output.

## 3. Error analysis

The selected model had **27 incorrect records out of 200** (13.5%). The weakest fields were priority (**90.0%**), `needs_human` (**94.0%**) and category (**97.0%**); amount was 98.5%, date 99.5%, and transaction ID, channel and language were each 100% in the reported field analysis. The weakest categories were refund (55 examples; 76.36% exact match), fraud (15; 80.00%) and payment_failed (53; 83.02%). The ten first dev errors have been reviewed and explained in `dev_error_analysis_first10.csv`. Common patterns were over/under-prioritization around the ₹5,000/₹50,000 cutoffs, failure to propagate P1 into `needs_human`, repeat-contact escalation, confusing card delivery with card payments, and confusing a stuck customer-initiated payment with unauthorized fraud.

## 4. Test inference and artifact validation

The final inference file contains **400 lines**, one per test ID (`ts-00001` through `ts-00400`), with the required outer `id` and raw `output` fields. The notebook reports exact 8-key structure validation **400/400** and a reproducibility check of **20/20 identical outputs**. The first raw output contains `txn_date: "2026-07-00"`, which is not a valid calendar date. It is retained unmodified because the assessment requires the raw model output; it should be disclosed rather than silently post-processed. The chosen PEFT adapter is `adapter/` and its run metadata identify E2.

## 5. What I would do next

Prioritize rule-boundary examples for priority cutoffs and P1 escalation; repeat-contact examples; distinguishing card-delivery questions from card transactions; and separating unauthorized fraud from customer-initiated payment failures. Add targeted validation for calendar dates, keep greedy decoding settings consistent with `do_sample=False`, and evaluate on a fresh held-out set before further tuning. Do not post-process predictions unless the assessment explicitly permits it.

## 6. AI tools used

ChatGPT assisted with interpreting the assessment specification, debugging the Colab environment and notebook, drafting code/documentation, and explaining dev errors. Google Colab/T4 executed the data audit, training, evaluation and test inference. The reported scores and predictions are taken from the generated assessment outputs.