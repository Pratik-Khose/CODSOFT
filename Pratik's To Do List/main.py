import tkinter
import tkinter.messagebox
import pickle
from datetime import datetime

root = tkinter.Tk()

root.title("To-Do List by Pratik")

print("Enjoy your own simple To-do List !!!")


def add_task():
    task = entry_task.get()
    due_date = entry_date.get()

    if task != "":
        if due_date:
            try:
                due_date = datetime.strptime(due_date, '%d-%m-%Y')
                task_with_date = f"{task} (Due: {due_date.strftime('%d-%m-%Y')})"
            except ValueError:
                tkinter.messagebox.showwarning("Warning!", "Invalid date format. Please use DD-MM-YYYY.")
                return
        else:
            task_with_date = task

        listbox_tasks.insert(tkinter.END, task_with_date)
        entry_task.delete(0, tkinter.END)
        entry_date.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning("Warning!", "You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning("Warning!", "You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning("Warning!", "Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, tkinter.END)
    pickle.dump(tasks, open("tasks.dat", "wb"))

frame_tasks = tkinter.Frame(root)

frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)

listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)

scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)

entry_task.pack()

label_date = tkinter.Label(root, text="Due Date (DD-MM-YYYY):")

label_date.pack()

entry_date = tkinter.Entry(root, width=20)

entry_date.pack()

button_add_task = tkinter.Button(root, text="ADD TASK", font=("Comic Sans MS", 12, "bold"), width=48, command=add_task, bg="#3399ff" , fg="#ffffff")

button_add_task.pack()

button_delete_task = tkinter.Button(root, text="DELETE TASK", font=("Comic Sans MS", 12, "bold"), width=48, command=delete_task, bg="#FF4500" , fg="#ffffff")

button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="LOAD TASK", font=("Comic Sans MS", 12, "bold"), width=48, command=load_tasks, bg="#ff9900" , fg="#ffffff")

button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="SAVE TASK", font=("Comic Sans MS", 12, "bold"), width=48, command=save_tasks, bg="#00cc00" , fg="#ffffff")

button_save_tasks.pack()

root.mainloop()
