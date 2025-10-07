# Simple To-Do List Program

tasks = []  # list to store all tasks

def addTask():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!\n")

def viewTasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()  # blank line for spacing

def removeTask():
    viewTasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Task '{removed}' removed successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def exitProgram():
    print("Exiting program... Goodbye!")
    exit()

def main():
    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            viewTasks()
        elif choice == "3":
            removeTask()
        elif choice == "4":
            exitProgram()
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()