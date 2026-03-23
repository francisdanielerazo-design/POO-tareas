import tkinter as tk
from tkinter import ttk, messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")
        self.root.geometry("700x400")

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # ===== LISTA =====
        frame_lista = tk.LabelFrame(main_frame, text="Eventos")
        frame_lista.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # ===== ENTRADAS =====
        frame_entrada = tk.LabelFrame(main_frame, text="Nuevo Evento")
        frame_entrada.pack(fill="x")

        tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
        self.fecha = tk.Entry(frame_entrada)
        self.fecha.grid(row=0, column=1)

        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2)
        self.hora = tk.Entry(frame_entrada)
        self.hora.grid(row=0, column=3)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0)
        self.descripcion = tk.Entry(frame_entrada, width=40)
        self.descripcion.grid(row=1, column=1, columnspan=3)

        # ===== BOTONES =====
        frame_botones = tk.Frame(main_frame)
        frame_botones.pack(fill="x")

        tk.Button(frame_botones, text="Agregar", command=self.agregar).pack(side="left")
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar).pack(side="left")
        tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right")

    def agregar(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        desc = self.descripcion.get()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Error", "Llena todos los campos")
            return

        self.tree.insert("", "end", values=(fecha, hora, desc))

    def eliminar(self):
        item = self.tree.selection()
        if item:
            self.tree.delete(item)
        else:
            messagebox.showwarning("Error", "Selecciona un evento")


root = tk.Tk()
app = AgendaApp(root)
root.mainloop()