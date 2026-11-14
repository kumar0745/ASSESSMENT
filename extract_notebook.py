"""Decompress notebook.ipynb.gz into notebook.ipynb."""
from pathlib import Path
import gzip

source = Path("notebook.ipynb.gz")
target = Path("notebook.ipynb")
if not source.exists():
    raise SystemExit("notebook.ipynb.gz is missing; run this script from the repository folder.")
with gzip.open(source, "rb") as compressed, target.open("wb") as output:
    output.write(compressed.read())
print(f"Created {target.resolve()}")
