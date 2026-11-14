# NimbusPay Ticket Triage — VIMA3YA ML Intern Assessment

**Repository:** `kumar0745/ASSESSMENT`  
**Base model:** `Qwen/Qwen2.5-1.5B-Instruct`  
**Method:** PEFT LoRA / QLoRA  
**Target runtime:** Google Colab NVIDIA T4

This repository contains the assessment notebook, schema, scorer, data-cleaning log, report and execution evidence.

## Run the notebook

1. Open `notebook.ipynb` in Google Colab (or extract it from `notebook.ipynb.gz` with `python extract_notebook.py`).
2. Select Runtime → Change runtime type → T4 GPU.
3. Run from the first cell. The setup checks CUDA and runs a real NF4 smoke test before training.
4. Upload the original `training_assessment.zip` when prompted. The source assessment archive and train/dev/test inputs are intentionally excluded from this repository.
5. Let all baseline, training, experiment, dev-evaluation and test-inference cells complete.
6. Download the executed notebook with cell outputs, the generated submission ZIP, and inspect every required output.

## Verified progress (2026-11-14)

The supplied screenshots show:
- CUDA runtime detected: NVIDIA Tesla T4, driver 580.82.07, CUDA 13.0.
- Dataset audit: 1,420 parseable raw training rows, 1,420 cleaned rows, 200 development rows and 400 test rows.
- Cleaning log generated, with visible sample fixes/drops.
- Training was still **in progress** in the captured screenshot: `E1_raw_qlora_r8`, step 71/264, epoch 0.79/3. The screenshot shows training loss 0.0487 at step 70.

These screenshots prove environment setup, data audit and a training-in-progress state only. They do **not** establish a completed experiment, final model selection, final accuracy or successful hidden-test inference.

## Assessment submission status

The following are the required final deliverables:
- `README.md`: model ID, 4-bit loading choice and one-line measured best result.
- `adapter/adapter_config.json` and `adapter/adapter_model.safetensors`: final PEFT adapter.
- `notebook.ipynb`: executed Colab notebook **with outputs** and reproducible final model/test prediction workflow.
- `report.md` or `report.pdf`: maximum 3 pages with audit, experiment table, error analysis, next steps and AI-tool disclosure.
- `cleaning_log.csv`: `id,action,reason`.
- `predictions_test.jsonl`: exactly one raw model output per test ID (400 lines).

At the moment, GPU training has been observed in progress, but completed experiment metrics, final adapter, final 400 predictions and the executed notebook with saved outputs have not yet been supplied. They are deliberately not fabricated or represented as complete. After the Colab run finishes, replace/update the relevant files using the actual generated artifacts and measured results.

## Evidence

- `evidence_gpu.jpg` — T4 GPU and CUDA runtime.
- `evidence_audit.jpg` — data audit and cleaning log.
- `evidence_training_progress.jpg` — E1 training progress (not final result).

## Data and submission hygiene

Keep this repository private until the assessment deadline rules permit publication. Do not commit the original assessment ZIP, raw train/dev/test datasets or base-model weights. Upload the final adapter and predictions only as permitted by the assessment instructions.
