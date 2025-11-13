import csv

FILENAME = "students.csv"


def add_student():
    """Adds a new student to the CSV file."""
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    grade = input("Enter student grade: ").strip()

    if not name:
        print("Name cannot be empty. Student not added.")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])

    print("Student record added successfully!")


def view_students():
    """Displays all students from the CSV file."""
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            students = list(reader)

        if not students:
            print("\nNo student records found.")
            return

        print("\nStudent Records:")
        print(f"{'Name':<20}{'Age':<6}{'Grade'}")
        print("-" * 35)
        for student in students:
            # handle rows with missing columns gracefully
            name = student[0] if len(student) > 0 else ""
            age = student[1] if len(student) > 1 else ""
            grade = student[2] if len(student) > 2 else ""
            print(f"{name:<20}{age:<6}{grade}")

    except FileNotFoundError:
        print("\nNo student records found.")


def search_student():
    """Searches for a student by name (case-insensitive)."""
    search_name = input("Enter student name to search: ").strip().lower()
    if not search_name:
        print("Please enter a name to search.")
        return

    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            found = False
            for student in reader:
                if len(student) == 0:
                    continue
                if student[0].strip().lower() == search_name:
                    age = student[1] if len(student) > 1 else ""
                    grade = student[2] if len(student) > 2 else ""
                    print(f"\nFound: Name: {student[0]}, Age: {age}, Grade: {grade}")
                    found = True
                    break

        if not found:
            print("Student not found!")

    except FileNotFoundError:
        print("\nNo student records found.")


# Main program loop
def main():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
