# Final Colab results — 14 November 2026

Source: uploaded executed Colab notebook, `nimbuspay_submission_artifacts.zip`, and final result screenshots.

## Environment and data audit
- NVIDIA Tesla T4; driver 580.82.07; CUDA 13.0.
- Input training rows: 1,445; retained: 1,420; dropped malformed targets: 25.
- Unique rows repaired: 157; cleaning actions: 182 (157 fixes, 25 drops).
- Development rows: 200; test rows: 400.

## Baselines (dev, n=200)
- Fixed-prompt baseline: exact match 0.0%, mean field accuracy 0.0%, JSON-valid 0.0%.
- Rules-in-prompt reference: exact match 0.5%, mean field accuracy 8.6875%, JSON-valid 14.0%.

## All five completed experiment runs

| Run | Dev exact match | Mean field accuracy | JSON valid | Peak GPU GB | Training min |
|---|---:|---:|---:|---:|---:|
| E1 raw QLoRA r8 | 74.50% | 95.6875% | 100% | 3.004 | 23.56 |
| E1 clean QLoRA r8 | 83.50% | 97.1875% | 100% | 3.003 | 23.89 |
| E2 clean LoRA FP16 r8 | **86.50%** | **97.3750%** | **100%** | 3.899 | **18.15** |
| E3 clean QLoRA r16 | 81.50% | 96.8125% | 100% | 3.066 | 24.30 |
| E4 clean balanced QLoRA r8 | 78.50% | 96.0625% | 100% | 3.003 | 24.43 |

Selected model: `E2_clean_lora_fp16_r8`, trained on clean data, rank 8, **FP16 (not 4-bit)**. It achieved 173/200 exact dev matches and 97.375% mean field accuracy. The four QLoRA variants used 4-bit loading.

## Error analysis
- Selected model errors: 27/200 (13.5%).
- Weakest fields: priority 90.0%, needs_human 94.0%, category 97.0%.
- Weakest categories: refund 76.36% exact (n=55), fraud 80.00% (n=15), payment_failed 83.02% (n=53).
- Ten actual dev error rows and their written explanations are in `dev_error_analysis_first10.csv`.

## Test output verification
- `predictions_test.jsonl`: exactly 400 JSONL records, 400 unique IDs, outer fields `id` and `output`.
- Inner 8-key structure validation: 400/400.
- Reproducibility check: 20/20 identical outputs.
- The raw output for `ts-00001` contains `txn_date: "2026-07-00"`, which is not a valid calendar date. It was preserved as raw model output and disclosed in the report; it was not silently post-processed.

## Final deliverables still requiring manual binary upload
The adapter config is in `adapter/adapter_config.json`; its companion 36,981,072-byte `adapter_model.safetensors` must also be committed under `adapter/`. The current GitHub integration can create text files and notebook commits but cannot transfer this binary weight file, so upload it through GitHub's browser interface. The 89,730-byte `predictions_test.jsonl` is also included in the downloaded output bundle; upload this exact raw file at the repository root if it is not present in the file tree.
