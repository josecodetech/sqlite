import tkinter as tk
from tkinter import messagebox

class AgendaGUI:
    def __init__(self, raiz, manejador_db):
        self.raiz = raiz
        self.raiz.title("Agenda de contactos")
        self.db = manejador_db
        # crear widgets
        self.etiqueta_nombre = tk.Label(raiz, text='Nombre: ')
        self.entrada_nombre = tk.Entry(raiz)
        self.etiqueta_telefono = tk.Label(raiz, text='Teléfono: ')
        self.entrada_telefono = tk.Entry(raiz)
        self.boton_agregar = tk.Button(raiz, text='Agregar contacto',command=self.agregar_contacto)
        self.boton_listar = tk.Button(raiz,text="Listar contactos",command=self.listar_contactos)
        # posicionar widgets
        self.etiqueta_nombre.grid(row=0, column=0)
        self.entrada_nombre.grid(row=0, column=1)
        self.etiqueta_telefono.grid(row=1, column=0)    
        self.entrada_telefono.grid(row=1, column=1)
        self.boton_agregar.grid(row=2, column=0)
        self.boton_listar.grid(row=2, column=1)
    def agregar_contacto(self):
        nombre = self.entrada_nombre.get()
        telefono = self.entrada_telefono.get()
        if nombre and telefono:
            self.db.agregar_contacto(nombre, telefono)
            messagebox.showinfo("Agregar contacto", "Contacto agregado correctamente") 
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_telefono.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Debe ingresar nombre y teléfono")   
    def listar_contactos(self):
        contactos = self.db.listar_contactos()
        lista = "\n".join([f"{c[1]}:{c[2]}" for c in contactos])
        messagebox.showinfo("Contactos", lista)
        