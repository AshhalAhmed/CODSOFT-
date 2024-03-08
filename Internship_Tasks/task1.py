                                # TASK1
# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists
tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append(task_name)
    print("Task added successfully.")

def view_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def update_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter task number to update: ")) -1
        if 0 <= task_index < len(tasks):
            new_task_name = input("Enter new task name: ")
            tasks[task_index] = new_task_name
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to update.")

def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
