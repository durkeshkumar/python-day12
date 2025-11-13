# quiz_score_manager.py
import csv
import os

FILENAME = "scores.csv"
FIELDNAMES = ["Name", "Subject", "Score"]


def ensure_file_with_header():
    """Create the CSV file with header if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_score():
    """Prompt user and append a new score row to the CSV file."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty. Score not added.")
        return

    subject = input("Enter subject: ").strip()
    if not subject:
        print("Subject cannot be empty. Score not added.")
        return

    score_input = input("Enter score (numeric): ").strip()
    try:
        score = float(score_input)
    except ValueError:
        print("Invalid score. Please enter a numeric value.")
        return

    ensure_file_with_header()
    with open(FILENAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({"Name": name, "Subject": subject, "Score": f"{score:.2f}"})

    print("Score added successfully!")


def view_scores():
    """Read and display all scores from the CSV file."""
    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print("\nNo scores found. Add some first.")
        return

    if not rows:
        print("\nNo scores recorded yet.")
        return

    print("\nAll Scores:")
    print(f"{'No.':<4}{'Name':<20}{'Subject':<15}{'Score'}")
    print("-" * 50)
    for i, row in enumerate(rows, start=1):
        name = row.get("Name", "")
        subject = row.get("Subject", "")
        score = row.get("Score", "")
        print(f"{i:<4}{name:<20}{subject:<15}{score}")


def search_student():
    """Search for scores by student name (case-insensitive) and display all matches."""
    search_name = input("Enter student name to search: ").strip().lower()
    if not search_name:
        print("Please enter a name to search.")
        return

    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.DictReader(f)
            matches = [row for row in reader if row.get("Name", "").strip().lower() == search_name]
    except FileNotFoundError:
        print("\nNo scores found.")
        return

    if not matches:
        print("No records found for that student.")
        return

    print(f"\nScores for '{search_name}':")
    print(f"{'No.':<4}{'Name':<20}{'Subject':<15}{'Score'}")
    print("-" * 50)
    for i, row in enumerate(matches, start=1):
        print(f"{i:<4}{row.get('Name',''):<20}{row.get('Subject',''):<15}{row.get('Score','')}")


def main():
    ensure_file_with_header()
    while True:
        print("\nQuiz Score Manager")
        print("1. Add Score")
        print("2. View All Scores")
        print("3. Search Student Scores")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_score()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
