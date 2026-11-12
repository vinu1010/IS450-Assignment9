# IS450-Assignment9

## Feature specification
**Name:** Save and load expenses (JSON file)

**Purpose:** Keep expenses between runs so data is not lost when the program closes.

**Expected behavior:** On startup the program loads `expenses.json` if it exists. Menu option 5 ("Save expenses to file") writes the current list to `expenses.json`. A missing, corrupted, or hand-edited file must not crash the program.

**Test cases:**
1. Add an expense, save, quit, restart -> the expense is still listed.
2. No `expenses.json` present -> program starts empty with no error.
3. `expenses.json` contains invalid text (`{not json`) -> a message is shown and the program starts empty.
4. `expenses.json` contains bad entries (negative amount, missing fields, wrong types) -> bad entries are skipped and valid ones load.

## What changed
- Added `import json` and a `DATA_FILE` constant (`expenses.json`).
- Added `save_expenses()`, which writes the list to the file and handles file-write errors.
- Added `load_expenses()`, which runs at startup, handles a missing or corrupt file, and checks each entry before accepting it.
- Menu: new option 5 "Save expenses to file"; Quit moved to option 6.
- Added a `.gitignore` so the `expenses.json` data file is not committed.

## Tests performed
| # | Test | Result |
|---|------|--------|
| 1 | Save, quit, restart | Pass: expense reloaded |
| 2 | No file present | Pass: starts empty, no error |
| 3 | Corrupt file (`{not json`) | Pass: message shown, starts empty |
| 4 | Bad entries in file | Pass: only the valid entry loaded |

## How AI was used
Gave Claude the feature specification above along with my existing `main.py` and asked it to implement the feature. Claude wrote `save_expenses()`, `load_expenses()`, and the menu changes. Then read the full diff, ran all four test cases, and [accepted the code as written / changed ___ because ___].

## Final review
Checked the **Files changed** tab and confirmed that only `main.py` and `.gitignore` were modified.
