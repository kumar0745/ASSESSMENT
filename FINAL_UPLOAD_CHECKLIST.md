# Final two-file upload check

The executed notebook and measured report/results are in this private repository. The following two required output files are prepared locally and must be added at the repository root/paths below before the repository satisfies every required deliverable.

| Local file | Required repository path | Size | SHA-256 |
|---|---|---:|---|
| Selected PEFT weight file | `adapter/adapter_model.safetensors` | 36,981,072 bytes | `ebafff5e7c71c74c5e449373ef9020fbb8ba4cfec706a905afdd7928038762f1` |
| Test predictions | `predictions_test.jsonl` | 89,730 bytes | `7f8a24b2639fd5f616902584b5a8379b2702c6f48d2b11fc1c44e68dd3f7fd20` |

The adapter configuration `adapter/adapter_config.json` is already committed. The local bundle `ASSESSMENT_manual_upload_remaining.zip` contains both files plus this instruction in matching folder paths.

## Upload through GitHub

1. Open this private repository and select **Add file → Upload files**.
2. Extract `ASSESSMENT_manual_upload_remaining.zip` locally.
3. Upload `adapter/adapter_model.safetensors` into the existing `adapter/` directory and `predictions_test.jsonl` at the repository root.
4. Commit to `main`.
5. Confirm that the file tree shows both exact paths.

Do not rename, edit, reformat or post-process the 400 raw model predictions. The first prediction contains a raw date value `2026-07-00`; this issue is disclosed in `report.md` and preserved as generated. Keep the repository private until the assessment deadline rules permit publication.
