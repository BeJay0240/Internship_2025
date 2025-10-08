class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.description}"

def add_task(tasks, description):
    tasks.append(Task(description))
    print(f"Task '{description}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print("------------------")

def mark_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = True
        print(f"Task '{tasks[task_index].description}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task.description}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
                mark_completed(tasks, task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks(tasks)
            try:
                task_num = int(input("Enter the number of the task to delete: ")) - 1
                delete_task(tasks, task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()