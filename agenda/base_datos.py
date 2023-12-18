import sqlite3
class BaseDatosContactos:
    def __init__(self, nombre_db="contactos.db"):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()
    def crear_tabla(self):
        consulta = """CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL)"""
        self.cursor.execute(consulta)
        self.conexion.commit()
    def agregar_contacto(self, nombre, telefono):
        consulta = "INSERT INTO contactos (nombre, telefono) VALUES (?, ?)"
        self.cursor.execute(consulta, (nombre, telefono))
        self.conexion.commit()
    def listar_contactos(self):
        consulta = "SELECT * FROM contactos"
        self.cursor.execute(consulta)
        return self.cursor.fetchall()
    