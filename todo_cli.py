"""Simple To-Do CLI Application

Allows the user to add, view, mark complete, and remove tasks.
"""


def load_tasks(file_name="tasks.txt"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks, file_name="tasks.txt"):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\nTODO MENU")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task done")
    print("4. Remove task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark done.")
                continue
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] = f"[Done] {tasks[index]}"
                save_tasks(tasks)
                print("Task updated.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            if not tasks:
                print("No tasks to remove.")
                continue
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
