Run the Edit Agent to process unhandled PDFs in `raw/` and generate wiki pages.

## Usage
- `/ingest` — process all pending PDFs across every subject
- `/ingest 자료구조` — process only PDFs under `raw/자료구조/`

## Steps

1. Check which PDFs in `raw/` have not yet been processed (no corresponding page in `wiki/pages/`).
2. Run the Edit Agent:

If `$ARGUMENTS` is empty:
```bash
.venv/bin/python agents/edit_agent.py --ingest
```

If `$ARGUMENTS` is a subject name (e.g. `자료구조`):
```bash
.venv/bin/python agents/edit_agent.py --ingest --subject "$ARGUMENTS"
```

3. Report the result: how many pages were created, which files were processed, and whether any errors occurred.
4. If new pages were created, remind the user to open `http://localhost:8000` to browse them.
