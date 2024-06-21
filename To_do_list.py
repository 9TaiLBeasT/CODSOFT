import tkinter as tk
from tkinter import messagebox

# Function to enter the task in the Listbox
def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(tk.END, input_text)
            root1.destroy()

    root1 = tk.Toplevel()
    root1.title("Add Task")
    root1.geometry("400x150")
    root1.config(bg="#f0f0f0")

    entry_task = tk.Text(root1, width=40, height=4, font=("Helvetica", 12))
    entry_task.pack(padx=10, pady=10)

    button_temp = tk.Button(root1, text="Add Task", command=add, bg="#4CAF50", fg="white", font=("Helvetica", 12), bd=0, padx=10, pady=5)
    button_temp.pack(pady=10)

# Function to delete task from the Listbox
def deletetask():
    try:
        selected = listbox_task.curselection()[0]
        listbox_task.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning!", "Please select a task to delete.")

# Function to mark the task completed
def markcompleted():
    try:
        marked = listbox_task.curselection()[0]
        temp_marked = listbox_task.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_task.delete(marked)
        listbox_task.insert(marked, temp_marked)
    except IndexError:
        messagebox.showwarning("Warning!", "Please select a task to mark as completed.")

# Creating the initial window
window = tk.Tk()
window.title("TO-DO List App")
window.geometry("600x500")
window.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(window, text="To-Do List App", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Frame widget to hold the listbox and the scrollbar
frame_task = tk.Frame(window, bg="#f0f0f0")
frame_task.pack(pady=10)

# To hold items in a listbox
listbox_task = tk.Listbox(frame_task, bg="white", fg="black", height=15, width=60, font=("Helvetica", 12), selectbackground="#4CAF50", selectforeground="white")
listbox_task.pack(side=tk.LEFT)

# Scrollbar in case the total list exceeds the size of the given window
scrollbar_task = tk.Scrollbar(frame_task)
scrollbar_task.pack(side=tk.RIGHT, fill=tk.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button widgets
entry_button = tk.Button(window, text="Add Task", width=50, command=entertask, bg="#4CAF50", fg="white", font=("Helvetica", 12), bd=0, padx=10, pady=5)
entry_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Selected Task", width=50, command=deletetask, bg="#f44336", fg="white", font=("Helvetica", 12), bd=0, padx=10, pady=5)
delete_button.pack(pady=5)

mark_button = tk.Button(window, text="Mark as Completed", width=50, command=markcompleted, bg="#2196F3", fg="white", font=("Helvetica", 12), bd=0, padx=10, pady=5)
mark_button.pack(pady=5)

window.mainloop()
