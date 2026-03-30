import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Lista para almacenar tareas
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    listbox.delete(0, tk.END)
    for tarea, completada in tareas:
        if completada:
            listbox.insert(tk.END, "✔ " + tarea)
        else:
            listbox.insert(tk.END, tarea)

# Añadir tarea
def añadir_tarea(event=None):
    tarea = entry.get().strip()
    if tarea == "":
        messagebox.showwarning("Aviso", "Escribe una tarea")
        return
    tareas.append((tarea, False))
    entry.delete(0, tk.END)
    actualizar_lista()

# Marcar como completada
def completar_tarea():
    try:
        index = listbox.curselection()[0]
        tarea, completada = tareas[index]
        tareas[index] = (tarea, not completada)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea")

# Eliminar tarea
def eliminar_tarea():
    try:
        index = listbox.curselection()[0]
        tareas.pop(index)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea")

# Evento doble clic para completar
def doble_click(event):
    completar_tarea()

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Permitir añadir con Enter
entry.bind("<Return>", añadir_tarea)

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=añadir_tarea)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_delete.pack(pady=5)

# Lista de tareas
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Evento doble clic
listbox.bind("<Double-Button-1>", doble_click)

# Ejecutar app
root.mainloop()