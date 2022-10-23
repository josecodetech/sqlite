import os
from tkinter import messagebox


def archivar(nombreArchivo, fecha, texto):
    try:
        archivo = nombreArchivo+".txt"
        escritura = open(archivo, "w")
        fechaTexto = fecha
        escritura.write(fechaTexto)
        escritura.write(texto)
        escritura.close()
    except:
        textoMensaje = "Error con el archivo de texto"
        messagebox.showerror("Error archivo", textoMensaje)


if __name__ == '__main__':
    texto = 'Hola esto es una prueba'
    archivar("pruebas", "23/10/22", texto)
