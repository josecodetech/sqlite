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


def consultarDatos01(conexion, cursor):
    sentencia = "SELECT * FROM usuarios"
    resultado = cursor.execute(sentencia)
    # print(cursor.fetchall())
    # print(resultado)
    for fila in resultado:
        print(fila)
    conexion.close()


def consultarDatos(conexion, cursor):
    sentencia = "SELECT id,usuario,email FROM usuarios"  # LIMIT 2
    resultado = cursor.execute(sentencia)

    # conexion.close()
    return resultado


def consultarDatosId(conexion, cursor, id):
    sentencia = f"SELECT usuario,email FROM usuarios WHERE id={id}"
    resultado = cursor.execute(sentencia)
    return resultado


if __name__ == '__main__':
    con, cursor = conectar()
    # print(con)
    # print(cursor)
    #crearTabla(con, cursor)
    #insertarDatos(con, cursor)
    datos = [('ANTONIO', 'KDFA@GMAIL.COM', '23DJK'),
             ('ALBERTO', 'DKJFKJ@GMAIL.COM', 'DKJFK2')]
    #insertarDatos(con, cursor, datos)
    resultado = consultarDatos(con, cursor)
    for fila in resultado:
        print("*"*100)
        print("\n")
        print("ID: ", fila[0])
        print("Nombre: ", fila[1])
        print("Email: ", fila[2])
        print("\n")
    resultado = consultarDatosId(con, cursor, 15)
    print(resultado)
    for fila in resultado:
        print(fila)
