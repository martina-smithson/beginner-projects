# To-Do list app

tasks = []

def show_menu():
    print("\nTodo List Menu:")
    print("1. View Task")
    print("2. Add Tasks")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print(f'Task "{new_task}" added!')

def remove_task():
    if not tasks:
        print("No tasks to remove!")
        return
   
    # show tasks
    view_tasks()

    # ask for task number to remove
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f'Task "{removed_task}" removed!')
    else:
        print("Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")
