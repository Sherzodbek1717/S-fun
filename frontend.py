import backend
import tkinter as tk

# Create an empty list to store tasks
tasks = []

# Define the functions for adding, editing, and deleting tasks
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, tasks[task_number])
        task_entry.focus()
        add_button.config(state=tk.DISABLED)
        save_button.config(state=tk.NORMAL)

def save_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        task = task_entry.get()
        tasks[task_number] = task
        task_listbox.delete(task_number)
        task_listbox.insert(task_number, task)
        task_entry.delete(0, tk.END)
        add_button.config(state=tk.NORMAL)
        save_button.config(state=tk.DISABLED)

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_number = selected_index[0]
        task_listbox.delete(task_number)
        tasks.remove(tasks[task_number])

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Create the task listbox and scrollbar
task_frame = tk.Frame(root)
task_listbox = tk.Listbox(task_frame, width=40, font=("Arial", 12))
task_scrollbar = tk.Scrollbar(task_frame, orient=tk.VERTICAL)
task_listbox.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=task_listbox.yview)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
task_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_frame.pack(fill=tk.BOTH, padx=5, pady=5)

# Create the task entry field and buttons
input_frame = tk.Frame(root)
task_label = tk.Label(input_frame, text="Task:", font=("Arial", 14))
task_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
add_button = tk.Button(input_frame, text="Add", font=("Arial", 14), command=add_task)
edit_button = tk.Button(input_frame, text="Edit", font=("Arial", 14), command=edit_task)
delete_button = tk.Button(input_frame, text="Delete", font=("Arial", 14), command=delete_task)
save_button = tk.Button(input_frame, text="Save", font=("Arial", 14), command=save_task, state=tk.DISABLED)
task_label.pack(side=tk.LEFT, padx=5)
task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
add_button.pack(side=tk.LEFT, padx=5)
edit_button.pack(side=tk.LEFT, padx=5)
delete_button.pack(side=tk.LEFT, padx=5)
save_button.pack(side=tk.LEFT, padx=5)
input_frame.pack(fill=tk.BOTH, padx=5, pady=5)

# Create the quit button
quit_button = tk.Button(root, text="Quit", font=("Arial", 14), command=root.quit)
quit_button.pack(pady=5)

# Start the main event loop
root.mainloop()

