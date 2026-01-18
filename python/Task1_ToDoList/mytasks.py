FILE_NAME = "task.txt"
tasks = []

# Load tasks
try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            task = line.strip()
            if task:
                tasks.append(task)
    print(f"Loaded {len(tasks)} task(s).")
except FileNotFoundError:
    print("No saved tasks found. Starting fresh.")


def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def create_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append(title)
    save_tasks()
    print(f"Task added: {title}")


def track_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def update_task():
    if not tasks:
        print("No tasks to update.")
        return

    track_tasks()
    try:
        idx = int(input("Enter task number to update: "))
        if idx < 1 or idx > len(tasks):
            print("Invalid task number.")
            return

        new_title = input("Enter new title: ").strip()
        if not new_title:
            print("New title cannot be empty.")
            return

        old = tasks[idx - 1]
        tasks[idx - 1] = new_title
        save_tasks()
        print(f"Updated: '{old}' → '{new_title}'")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    track_tasks()
    try:
        idx = int(input("Enter task number to delete: "))
        if idx < 1 or idx > len(tasks):
            print("Invalid task number.")
            return

        confirm = input(f"Delete '{tasks[idx - 1]}'? (y/n): ").lower().strip()
        if confirm == "y":
            removed = tasks.pop(idx - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Create Task")
    print("2. Track Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        create_task()
    elif choice == "2":
        track_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Tasks saved in task.txt.")
        break
    else:
        print("Invalid option. Choose 1–5.")
