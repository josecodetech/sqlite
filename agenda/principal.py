import tkinter as tk
from interfaz import AgendaGUI
from base_datos import BaseDatosContactos

def main():
    raiz = tk.Tk()
    manejador_db = BaseDatosContactos()
    app = AgendaGUI(raiz, manejador_db)
    raiz.mainloop()
if __name__=='__main__':
    main()