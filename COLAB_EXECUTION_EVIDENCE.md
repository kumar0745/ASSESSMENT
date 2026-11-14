# Colab Execution Evidence — 14 November 2026

This page transcribes the three screenshots supplied during the assessment run. The images were provided in the conversation; this text records only what is visibly readable in them.

## 1. GPU runtime

Visible `nvidia-smi` output:
- GPU: NVIDIA Tesla T4
- Driver: 580.82.07
- CUDA: 13.0
- GPU memory at capture: 155 MiB / 15,360 MiB
- GPU utilization at capture: 0%

**Interpretation:** A T4 GPU runtime was available at the time of the screenshot. The 0% utilization reading is a point-in-time idle snapshot and does not prove training was running at that exact instant.

## 2. Data audit

Visible notebook output:
- Parseable raw training rows: 1,420
- Cleaned training rows: 1,420
- Development rows: 200
- Test rows: 400
- A cleaning-log dataframe was displayed with `id`, `action`, and `reason` columns; sample rows include both fixes and a dropped malformed target.

This is consistent with auditing 1,445 input training records, dropping 25 malformed/truncated targets, and retaining 1,420 parseable rows. The data audit is evidence of preprocessing, not model performance.

## 3. Training progress (not a final result)

Visible training output:
- Run: `E1_raw_qlora_r8`
- Trainable parameters: 9,232,384
- Total parameters shown by this run: 897,848,832
- Progress: step 71 / 264
- Epoch: 0.79 / 3
- Throughput shown: approximately 0.19 iterations/second
- Training loss table showed 0.0487 at step 70.

**Status at screenshot:** Training was still in progress. This screenshot does not establish that E1 completed, that its dev evaluation succeeded, or that it is the best run.

## What is not established by these screenshots

The screenshots do not show:
- completed baseline exact-match / field-accuracy metrics;
- completion and dev scores for all five training configurations;
- the selected best run;
- ten reviewed development-set prediction errors;
- a saved final PEFT adapter;
- a validated `predictions_test.jsonl` with exactly 400 rows;
- an executed/downloaded notebook containing all completed run outputs.

Do not describe the assessment as complete until these artifacts and metrics have been generated and checked.
