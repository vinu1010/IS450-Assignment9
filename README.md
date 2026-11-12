# IS450-Assignment9

## Feature specification
**Name:** Delete an expense
**Purpose:** Remove mistaken entries without restarting the program.
**Expected behavior:** New menu option 5 shows the numbered list, asks for a number, asks "Are you sure? (y/n)", and deletes only on `y`. Invalid input does not crash.
**Test cases:** (1) delete #2 with `y` -> removed, totals update; (2) answer `n` -> nothing removed; (3) `0`, `99`, `abc` -> friendly message; (4) empty list -> "No expenses yet."

## What changed
Added `delete_expense()` and a new menu option; Quit moved to option 6.



