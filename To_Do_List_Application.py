import tkinter as tk
from tkinter import messagebox

# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    task_list.delete(0, tk.END)
    if not tasks:
        task_list.insert(tk.END, "Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            task_list.insert(tk.END, f"{i}. {task['task']} ({status})")

# Function to add a task to the to-do list
def add_task():
    task_name = task_entry.get()
    if task_name:
        task = {"task": task_name, "completed": False}
        tasks.append(task)
        task_entry.delete(0, tk.END)
        display_tasks()
        messagebox.showinfo("Task Added", f"Task '{task_name}' added to your to-do list.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as completed
def mark_completed():
    try:
        task_number = int(task_number_entry.get())
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            display_tasks()
            messagebox.showinfo("Task Completed", f"Task {task_number} marked as completed.")
        else:
            messagebox.showwarning("Invalid Task Number", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task():
    try:
        task_number = int(task_number_entry.get())
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            display_tasks()
            messagebox.showinfo("Task Removed", f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            messagebox.showwarning("Invalid Task Number", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

# Setting up the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Add Task Button
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Task List Display
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Task Number Entry
task_number_entry = tk.Entry(root, width=10)
task_number_entry.pack(pady=5)

# Mark Completed Button
mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_completed_button.pack(pady=5)

# Remove Task Button
remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

# Display Initial Tasks
display_tasks()

# Run the application
root.mainloop()
