# To-Do List using File Handling

def display_tasks():
    """Displays all tasks from the file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nNo tasks available.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks found. Start by adding new tasks!")


def add_task():
    """Adds a new task to the file."""
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")


def remove_task():
    """Removes a task from the file."""
    display_tasks()
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            return

        task_num = int(input("\nEnter the task number to remove: "))

        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("Task removed successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks available to remove.")


# Main program loop
while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
