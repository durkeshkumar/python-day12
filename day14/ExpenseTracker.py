# expense_tracker.py
from datetime import datetime

FILENAME = "expenses.txt"


def add_expense():
    """Prompt user and append a new expense (Category, Amount, Date) to the file."""
    category = input("Enter category (e.g., Food, Rent, Travel): ").strip()
    if not category:
        print("Category cannot be empty. Expense not added.")
        return

    amount_input = input("Enter amount (numeric): ").strip()
    try:
        # Convert to float and round to 2 decimal places for currency-like behavior
        amount = round(float(amount_input), 2)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_str = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            # Validate and normalize date input
            date_obj = datetime.strptime(date_input, "%Y-%m-%d")
            date_str = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD. Expense not added.")
            return

    # Write as CSV-like line: Category,Amount,Date
    with open(FILENAME, "a", newline="") as f:
        f.write(f"{category},{amount:.2f},{date_str}\n")

    print("Expense added successfully!")


def view_expenses():
    """Read and display all expenses from the file in a tabular form."""
    try:
        with open(FILENAME, "r", newline="") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("\nNo expenses found. Add some first.")
        return

    if not lines:
        print("\nNo expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print(f"{'No.':<4}{'Category':<15}{'Amount':<12}{'Date'}")
    print("-" * 45)
    for i, line in enumerate(lines, start=1):
        parts = line.split(",")
        cat = parts[0] if len(parts) > 0 else ""
        amt = parts[1] if len(parts) > 1 else "0.00"
        date = parts[2] if len(parts) > 2 else ""
        print(f"{i:<4}{cat:<15}{amt:<12}{date}")


def total_expenditure():
    """Calculate and print the total of all expense amounts (safely)."""
    try:
        with open(FILENAME, "r", newline="") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("\nNo expenses found. Total is 0.00")
        return

    total = 0.0
    for line in lines:
        parts = line.split(",")
        if len(parts) < 2:
            continue
        amt_str = parts[1].strip()
        try:
            # convert each amount to float carefully
            amt = float(amt_str)
            total += amt
        except ValueError:
            # skip malformed amounts
            continue

    # Format total with 2 decimals
    print(f"\nTotal expenditure: {total:.2f}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Get Total Expenditure")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenditure()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
