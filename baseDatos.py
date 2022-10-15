import sqlite3


def conectar():
    con = sqlite3.connect('pruebas.db')  # :memory
    cursor = con.cursor()
    return con, cursor


def crearTabla(conexion, cursor):
    sentencia = """
        CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY NOT NULL,
        USUARIO TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        CLAVE TEXT NOT NULL);
    """
    cursor.execute(sentencia)
    conexion.close()
    print('Tabla creada correctamente')


def insertarDatos(conexion, cursor, datos):
    #sentencia = "INSERT INTO usuarios (ID, USUARIO,EMAIL,CLAVE) VALUES(11,'JOSE','JOSECODETECH@GMAIL.COM','DJFKJ')"
    sentencia = "INSERT INTO usuarios VALUES (NULL,?,?,?)"
    #cursor.execute(sentencia, datos)
    cursor.executemany(sentencia, datos)
    # cursor.execute(sentencia)
    print("Datos insertados correctamente")
    conexion.commit()
    conexion.close()


if __name__ == '__main__':
    con, cursor = conectar()
    # print(con)
    # print(cursor)
    #crearTabla(con, cursor)
    #insertarDatos(con, cursor)
    datos = [('ANTONIO', 'KDFA@GMAIL.COM', '23DJK'),
             ('ALBERTO', 'DKJFKJ@GMAIL.COM', 'DKJFK2')]
    insertarDatos(con, cursor, datos)
