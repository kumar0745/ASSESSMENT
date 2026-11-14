# NimbusPay Ticket Triage — VIMA3YA ML Intern Assessment

**Base model:** `Qwen/Qwen2.5-1.5B-Instruct`  
**Selected run:** `E2_clean_lora_fp16_r8`  
**Selected configuration:** clean data, LoRA rank 8, FP16 (not 4-bit), unbalanced sampling  
**Measured dev results:** 86.50% exact match (173/200), 97.375% mean field accuracy, 100% JSON-valid  
**Runtime:** NVIDIA Tesla T4, CUDA 13.0

## Final measured experiment comparison

| Run | Dev exact match | Mean field accuracy | JSON valid | Peak GPU GB | Training min |
|---|---:|---:|---:|---:|---:|
| E1 raw QLoRA r8 | 74.50% | 95.6875% | 100% | 3.004 | 23.56 |
| E1 clean QLoRA r8 | 83.50% | 97.1875% | 100% | 3.003 | 23.89 |
| E2 clean LoRA FP16 r8 | **86.50%** | **97.3750%** | **100%** | 3.899 | **18.15** |
| E3 clean QLoRA r16 | 81.50% | 96.8125% | 100% | 3.066 | 24.30 |
| E4 clean balanced QLoRA r8 | 78.50% | 96.0625% | 100% | 3.003 | 24.43 |

The best run is FP16 LoRA; it was **not loaded in 4-bit**. The four QLoRA variants used 4-bit loading.

## Data and evaluation
- Training: 1,445 raw rows → 1,420 retained; 25 malformed/truncated targets dropped.
- Cleaning: 157 unique rows repaired, 182 log actions total (157 fixes, 25 drops).
- Dev: 200 records. Test: 400 records.
- Best model: 27/200 dev records incorrect. Weakest fields: priority 90%, needs_human 94%, category 97%.
- Weakest categories: refund 76.36% exact (n=55), fraud 80.00% (n=15), payment_failed 83.02% (n=53).
- Test inference: 400 records, 400 unique IDs, inner 8-key validation 400/400; reproducibility check 20/20 identical outputs.
- Raw prediction for `ts-00001` contains invalid date `2026-07-00`; preserved and disclosed rather than post-processed.

## Run the notebook
1. Open `notebook.ipynb` in Google Colab.
2. Select Runtime → Change runtime type → T4 GPU.
3. Upload the original assessment ZIP when prompted.
4. Run cells from top to bottom. The notebook records the audit, baselines, five training configurations, dev evaluation/error analysis and test inference.
5. Download `nimbuspay_submission_artifacts.zip` and the executed notebook from Colab for the actual assessment hand-in.

## Required deliverables
The assessment specifies: this README; PEFT adapter folder with `adapter_config.json` and `adapter_model.safetensors`; executed `notebook.ipynb` with outputs; a report up to three pages; `cleaning_log.csv`; and exactly 400 records in `predictions_test.jsonl`.

## Repository file status
Committed: executed `notebook.ipynb` with cell outputs, `report.md`, `cleaning_log.csv`, `experiment_results.csv`, `report_results.json`, `audit_summary.json`, `dev_error_analysis_first10.csv`, schema, scorer and execution notes. `adapter/adapter_config.json` is also committed.

**Manual final binary/file check:** The adapter weight file `adapter/adapter_model.safetensors` (36,981,072 bytes) and root `predictions_test.jsonl` (89,730 bytes) still need to be added through GitHub's browser upload unless they appear in the final tree. Do not claim the repository is submission-complete until both are visible under those exact paths.

Keep the repository private until the assessment deadline rules permit publication. Do not commit the original training assessment ZIP, raw train/dev/test datasets or base-model weights.
