"""Expense Tracker - Stage 2.

A small command-line program that lets a user record expenses, view them
(sorted or filtered), and see totals per category.

Stage 2 changes:
  * Added get_valid_amount(), which validates money input instead of crashing.
  * Added a "Filter / sort expenses" menu option (filter_and_sort_expenses()).

Mmanual-feature branch:
  * Added a "Delete expense" menu option (delete_expense()).
"""

# Each expense is stored as a dictionary: {"description": str, "category": str, "amount": float}
# All expenses live in this list while the program runs (nothing is saved to disk).
expenses = []


def get_valid_amount(prompt):
    """Keep asking until the user enters a positive number; return it as a float.

    Stage 1 used float(input(...)) directly, so typing "abc" crashed the
    program with a ValueError. try/except lets catch that error and ask again.
    """
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number, like 12.50.")
            continue

        # Reject zero/negative values because an expense should be a positive cost.
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        return amount


def get_non_empty(prompt):
    """Keep asking until the user types something other than blank spaces."""
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("This field cannot be empty.")


def add_expense():
    """Ask the user for expense details and store them in the expenses list."""
    description = get_non_empty("Description: ")
    # Categories are lowercased so "Food" and "food" are totaled together.
    category = get_non_empty("Category (e.g. food, rent, fun): ").lower()
    amount = get_valid_amount("Amount: $")

    expenses.append({"description": description, "category": category, "amount": amount})
    print("Expense added!")


def print_expense_list(expense_list):
    """Print a numbered list of the expenses passed in (shared by several menu options)."""
    # enumerate gives a friendly 1-based number for each row
    for number, expense in enumerate(expense_list, start=1):
        print(f"{number}. {expense['description']} ({expense['category']}) - ${expense['amount']:.2f}")


def view_expenses():
    """Print every expense that has been entered so far."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print_expense_list(expenses)


def filter_and_sort_expenses():
    """NEW feature: optionally filter by category, then sort by amount."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    category = input("Category to show (press Enter for all): ").strip().lower()

    # A list comprehension builds a new list so the original data is never changed.
    if category == "":
        results = list(expenses)
    else:
        results = [e for e in expenses if e["category"] == category]

    if len(results) == 0:
        print(f"No expenses found in category '{category}'.")
        return

    order = input("Sort by amount: (h)ighest first, (l)owest first, or Enter to skip: ").strip().lower()
    if order == "h":
        # key tells sorted() which value in each dictionary to compare
        results = sorted(results, key=lambda e: e["amount"], reverse=True)
    elif order == "l":
        results = sorted(results, key=lambda e: e["amount"])

    print_expense_list(results)


def delete_expense():
    """Let the user remove one expense by its displayed number, after confirming."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print_expense_list(expenses)
    choice = input("Number of the expense to delete: ").strip()

    # Reject anything that is not a whole number (letters, blanks, decimals).
    if not choice.isdigit():
        print("Please enter a whole number from the list.")
        return

    # The list shown to the user starts at 1, but Python lists start at 0,
    # so subtract 1 to get the real position.
    number = int(choice)
    if number < 1 or number > len(expenses):
        print(f"No expense numbered {number}.")
        return

    expense = expenses[number - 1]
    confirm = input(f"Delete '{expense['description']}' (${expense['amount']:.2f})? (y/n): ").strip().lower()
    if confirm == "y":
        expenses.pop(number - 1)
        print("Expense deleted.")
    else:
        print("Delete cancelled.")


def show_totals():
    """Print the overall total and the total spent in each category."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    # A dictionary maps each category name to a running total.
    # .get(category, 0) handles the first time a category is seen.
    totals = {}
    overall = 0
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
        overall += expense["amount"]

    print("\nSpending by category:")
    for category, total in totals.items():
        print(f"  {category}: ${total:.2f}")
    print(f"Overall total: ${overall:.2f}")


def main():
    """Show the menu repeatedly until the user chooses to quit."""
    # Repeat the menu until the user selects the exit option.
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Filter / sort expenses")
        print("4. Show totals")
        print("5. Delete expense")
        print("6. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_and_sort_expenses()
        elif choice == "4":
            show_totals()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-6.")


main()