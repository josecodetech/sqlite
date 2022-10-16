import sqlite3


def conectar():
    con = sqlite3.connect('alumnos.db')
    cursor = con.cursor()
    return con, cursor


def crearTabla(conexion, cursor):
    sentencia = """
        CREATE TABLE IF NOT EXISTS alumnos
        (ID INTEGER PRIMARY KEY NOT NULL,
        NOMBRE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        NOTA INTEGER NOT NULL)
    """
    cursor.execute(sentencia)
    conexion.close()
    return True


def insertarAlumno(conexion, cursor):
    nombre = input('Dime el nombre del alumno : ')
    email = input('Dime el email : ')
    nota = int(input('Que nota tiene ? '))
    sentencia = f"INSERT INTO alumnos VALUES (NULL,?,?,?)"
    datos = (nombre, email, nota)
    cursor.execute(sentencia, datos)
    conexion.commit()


def consultarAlumnos(conexion, cursor):
    sentencia = "SELECT id, nombre, email, nota FROM alumnos"
    resultado = cursor.execute(sentencia)

    return resultado


def modificarNota(conexion, cursor):
    id = input('Dime el identificador del alumno : ')
    nota = input('Dime la nota : ')
    sentencia = f"UPDATE alumnos set nota={nota} WHERE id={id}"
    cursor.execute(sentencia)
    conexion.commit()
    return True


def borrarAlumno(conexion, cursor):
    id = input('Dime el identificador del alumno a borrar :')
    sentencia = f"DELETE from alumnos WHERE id={id}"
    cursor.execute(sentencia)
    conexion.commit()
    return True


def menu():
    menu = """
          1. Insertar Dato alumno.
          2. Consultar alumnos.
          3. Modificar nota.
          4. Borra alumno.
          0. Salir.
          """
    print(menu)
    opcion = int(input())
    con, cursor = conectar()
    crearTabla(con, cursor)
    while True:
        if opcion == 1:
            con, cursor = conectar()
            insertarAlumno(con, cursor)
        elif opcion == 2:
            con, cursor = conectar()
            resultado = consultarAlumnos(con, cursor)
            for fila in resultado:
                print("*"*100)
                print("\n")
                print("ID: ", fila[0])
                print("Nombre: ", fila[1])
                print("Email: ", fila[2])
                print("Nota: ", fila[3])
                print("\n")
        elif opcion == 3:
            con, cursor = conectar()
            modificarNota(con, cursor)
        elif opcion == 4:
            con, cursor = conectar()
            borrarAlumno(con, cursor)
        elif opcion == 0:
            con.close()
            print("Adios, hasta pronto")
            break
        else:
            print("Indica una opcion valida")
        print(menu)
        opcion = int(input())


def principal():
    menu()


if __name__ == '__main__':
    principal()
