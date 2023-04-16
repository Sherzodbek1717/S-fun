# Create an empty list to store tasks
tasks = []

# Function to display the tasks
def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print()

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.\n")

# Function to edit an existing task
def edit_task():
    display_tasks()
    task_number = int(input("Enter the number of the task you want to edit: "))
    task = input("Enter the new task: ")
    tasks[task_number-1] = task
    print(f"Task {task_number} updated.\n")

# Function to delete an existing task
def delete_task():
    display_tasks()
    task_number = int(input("Enter the number of the task you want to delete: "))
    task = tasks.pop(task_number-1)
    print(f"Task '{task}' deleted from the list.\n")

# Main loop of the program
while True:
    print("Enter '1' to display the to-do list")
    print("Enter '2' to add a new task")
    print("Enter '3' to edit an existing task")
    print("Enter '4' to delete an existing task")
    print("Enter '5' to quit the program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        edit_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")
