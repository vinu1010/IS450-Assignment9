## Feature Development Comparison

Features: On manuel-feature (the one i did myself) I added a delete-expense option that removes an entry by its number after a y/n confirmation. On ai-feature (the one that was generated with AI) I added saving and loading expenses to a JSON file so data survives restarts.

Approach: I went off of the deliverable I prepared for the last assignment and added an addition for the first branch, then used AI (specifically Claude) to generate the 2nd branch additions. For the AI branch, I gave Claude the specification and my existing "main.py", and it produced "save_expenses()", "load_expenses()", and the menu changes.

Confidence: I felt more confident in  the save/load feature because it the tests covered more rough cases. Both branches changed the menu, which caused a merge conflict. I fixed it by keeping both options and renumbering the menu to 5 Delete, 6 Save, 7 Quit, then retested everything together.