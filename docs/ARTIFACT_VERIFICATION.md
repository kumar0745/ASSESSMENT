# Assessment artifact verification — 2026-11-18

This note records a read-only repository tree inspection. It does not replace the assessment's own submission checklist or a full download/hash verification.

## Present in the inspected default-branch root

- Executed notebook.ipynb
- report.md
- cleaning_log.csv
- experiment_results.csv
- report_results.json
- audit_summary.json
- dev_error_analysis_first10.csv
- SCHEMA.md and score.py
- adapter/adapter_config.json

## Not present at the expected paths in the inspected tree

- adapter/adapter_model.safetensors
- predictions_test.jsonl

The README reports that the expected adapter weights are 36,981,072 bytes and the predictions file is 89,730 bytes. Those files were not visible in the root/adapter directory listings inspected for this audit. This is a path-specific check, not proof that no copy exists elsewhere in Git history or another branch.

## Required before describing the repository as submission-complete

- [ ] Upload adapter/adapter_model.safetensors from the verified final run.
- [ ] Upload predictions_test.jsonl at the documented root path.
- [ ] Verify exactly 400 JSONL records and unique IDs.
- [ ] Verify every record against the schema and required field constraints.
- [ ] Re-run the repository scorer and compare the output with report_results.json.
- [ ] Record SHA-256 checksums for both uploaded artifacts.
- [ ] Confirm the notebook is executed and outputs correspond to the same adapter/configuration.
- [ ] Review assessment rules before changing repository visibility; the current README says to keep the repository private until permitted.

## Data and model handling

Do not commit the original assessment archive, raw private datasets, personal data, access tokens or base-model weights. Preserve the exact model/run/configuration identity in the report and do not substitute files from a different run.
