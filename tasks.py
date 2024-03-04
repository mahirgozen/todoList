import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Task:
    def __init__(self, title, description="", priority=0):
        self.title = title # Titre de la tâche
        self.description = description # Description de la tâche
        self.priority = priority # Priorité de la tâche (1 pour basse, 2 pour moyenne, 3 pour haute)

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nPriority: {self.priority}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App") # Titre de l'application

        self.tasks = [] # Liste des tâches

        self.task_frame = tk.Frame(root) # Cadre pour les tâches
        self.task_frame.pack(padx=10, pady=10)

        self.task_label = tk.Label(self.task_frame, text="Tasks:") # Étiquette pour les tâches
        self.task_label.grid(row=0, column=0, sticky="w")

        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=15) # Liste des tâches
        self.task_listbox.grid(row=1, column=0, rowspan=5)

        self.scrollbar = tk.Scrollbar(self.task_frame, orient="vertical", command=self.task_listbox.yview) # Barre de défilement pour la liste
        self.scrollbar.grid(row=1, column=1, rowspan=5, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)  # Bouton pour ajouter une tâche
        self.add_button.grid(row=1, column=2, padx=10)

        self.delete_button = tk.Button(self.task_frame, text="Delete Task", command=self.delete_task) # Bouton pour supprimer une tâche
        self.delete_button.grid(row=2, column=2, padx=10)

        self.display_button = tk.Button(self.task_frame, text="Display Tasks", command=self.display_tasks) # Bouton pour afficher les tâches
        self.display_button.grid(row=3, column=2, padx=10)

        self.exit_button = tk.Button(self.task_frame, text="Exit", command=root.quit) # Bouton pour quitter l'application
        self.exit_button.grid(row=4, column=2, padx=10)

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter the task title:")
        if title:
            description = simpledialog.askstring("Task Description", "Enter the task description (optional):")
            priority = simpledialog.askinteger("Task Priority", "Enter the task priority (1 for low, 2 for medium, 3 for high):")
            task = Task(title, description, priority)
            self.tasks.append(task)
            self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()  # Récupérer l'index de la tâche sélectionnée
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks to display.")
            return
        task_info = ""
        for task in self.tasks:
            task_info += str(task) + "\n\n" # Informations sur les tâches
        messagebox.showinfo("Tasks", task_info) # Afficher les tâches

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task.title) # Mettre à jour la liste des tâches

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
