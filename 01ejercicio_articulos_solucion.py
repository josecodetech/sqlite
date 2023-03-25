import sqlite3

def conectar():
    conexion=sqlite3.connect('articulos.db')
    cursor=conexion.cursor()
    #print("Conectado a BD")
    return conexion,cursor
def cerrar_conexion(conexion):
    conexion.close()
def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS ARTICULOS (IDENTIFICADOR INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT TEXT)')
    cerrar_conexion(conexion)
    #print("Tabla creada")
def carga_inicial():
    conexion, cursor = conectar()
    articulos =[
        (1235,"cuaderno",25,2.36),
        (1254,"boligrafo",100,0.90),
        (1345,"goma",75,0.50)
    ]  
    cursor.executemany('INSERT INTO ARTICULOS VALUES (?,?,?,?)',articulos)
    conexion.commit()
    cerrar_conexion(conexion)   
def insertar(articulo):
    conexion, cursor = conectar()
    cursor.execute('INSERT INTO ARTICULOS VALUES (?,?,?,?)',articulo)
    conexion.commit()
    cerrar_conexion(conexion)  
    print("Dato insertado")
def consultar():
    conexion, cursor = conectar()
    cursor.execute('SELECT * FROM ARTICULOS')
    articulos = cursor.fetchall()
    cerrar_conexion(conexion)
    return articulos
def actualizar(identificador,nombre,cantidad,importe):
    conexion, cursor = conectar()
    cursor.execute(f"UPDATE ARTICULOS SET NOMBRE='{nombre}',CANTIDAD={cantidad},IMPORTE={importe} WHERE IDENTIFICADOR={identificador}")
    print("Articulo actualizado")
    conexion.commit()
    cerrar_conexion(conexion)
def borrar(identificador):
    conexion, cursor = conectar()
    cursor.execute(f"DELETE FROM ARTICULOS WHERE IDENTIFICADOR={identificador}")
    conexion.commit()
    print("Articulo borrado")
    cerrar_conexion(conexion)
if __name__=='__main__':
    crear_tabla()
    #carga_inicial()
    #articulo = (1352, "lapiz", 150, 0.60)
    #insertar(articulo)
    #actualizar(1352,"Lapiz verde",149,0.55)
    articulos = consultar()
    for articulo in articulos:
        print(articulo[1])
    borrar(1352)
    print("*"*50)
    articulos = consultar()
    for articulo in articulos:
        print(articulo[1])