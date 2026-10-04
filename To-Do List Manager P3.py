import json
import os

FILE_NAME = "tasks.json"


# ---------- File Handling ----------

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading tasks file. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks.")


# ---------- Task Logic ----------

def add_task(tasks):
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== TO-DO LIST =====")

    for index, task in enumerate(tasks, start=1):
        status = "✓ Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {status}")


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)

        print(f"Deleted: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid number.")


def mark_task_done(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to mark as done: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


# ---------- Main Menu ----------

def main():
    tasks = load_tasks()

    while True:
        print("\n==============================")
        print("       TO-DO LIST MANAGER")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()