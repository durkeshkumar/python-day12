class InvalidMarksError(Exception):
    """Custom exception for invalid marks."""
    pass


def calculate_grade(marks):
    """Function to determine grade based on marks."""
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


# Taking input from the user
try:
    marks = float(input("Enter student marks (0-100): "))
    grade = calculate_grade(marks)
    print(f"Student Grade: {grade}")

except ValueError:
    print("Error: Please enter a valid number.")

except InvalidMarksError as e:
    print("Error:", e)
