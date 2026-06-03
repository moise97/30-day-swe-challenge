import json


TASKS_FILE = "tasks.json"


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_task(tasks):
    name = input("Enter task name: ")
    task = {"name": name, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {name}")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "x"
            print(f"{i + 1}. [{status}] {task['name']}")


def mark_done(tasks):
    view_tasks(tasks)

    num = int(input("Enter task number to mark done: "))

    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as done!")
    else:
        print("Invalid number")


def delete_task(tasks):
    view_tasks(tasks)

    num = int(input("Enter task number to delete: "))

    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid number")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again")


main()
