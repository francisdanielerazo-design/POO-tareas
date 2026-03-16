import tkinter as tk
from tkinter import ttk

# Función para agregar datos
def agregar_dato():
    dato = entrada.get()
    if dato != "":
        lista_datos.insert("", "end", values=(dato,))
        entrada.delete(0, tk.END)

# Función para limpiar datos
def limpiar_dato():
    seleccion = lista_datos.selection()
    for item in seleccion:
        lista_datos.delete(item)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Información")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Tabla para mostrar datos
lista_datos = ttk.Treeview(ventana, columns=("Dato"), show="headings")
lista_datos.heading("Dato", text="Información agregada")
lista_datos.pack(pady=10)

# Botón limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar seleccionado", command=limpiar_dato)
btn_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()