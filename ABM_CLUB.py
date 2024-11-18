import sqlite3
import os
from datetime import datetime

# Obtener la ruta del directorio actual donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'club.db')

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear las tablas (si no existen)
def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS integrantes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            numero_documento TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            telefono TEXT NOT NULL,
            domicilio TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actividades (
            ID_actividad INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_integrante INTEGER,
            tipo_actividad TEXT,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            FOREIGN KEY (ID_integrante) REFERENCES integrantes (ID)
        )
    ''')

# Función para agregar un integrante
def agregar_integrante():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_documento = input("Número de documento: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    telefono = input("Teléfono: ")
    domicilio = input("Domicilio: ")

    cursor.execute('''
        INSERT INTO integrantes (nombre, apellido, numero_documento, fecha_nacimiento, telefono, domicilio)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, numero_documento, fecha_nacimiento, telefono, domicilio))
    conn.commit()
    print("Integrante agregado correctamente.")

# Función para consultar los datos de los integrantes
def consultar_integrantes():
    cursor.execute('SELECT * FROM integrantes')
    integrantes = cursor.fetchall()
    for integrante in integrantes:
        print(integrante)

# Función para eliminar un integrante
def eliminar_integrante():
    id_integrante = int(input("ID del integrante a eliminar: "))
    cursor.execute('DELETE FROM integrantes WHERE ID = ?', (id_integrante,))
    conn.commit()
    print("Integrante eliminado correctamente.")

# Función para ordenar los integrantes por criterio
def ordenar_integrantes():
    print("Ordenar por:")
    print("1. Alfabético por nombre")
    print("2. Numérico por ID")
    print("3. Por edad")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        cursor.execute('SELECT * FROM integrantes ORDER BY nombre')
    elif opcion == 2:
        cursor.execute('SELECT * FROM integrantes ORDER BY ID')
    elif opcion == 3:
        cursor.execute('''
            
        ''')

    integrantes = cursor.fetchall()
    for integrante in integrantes:
        print(integrante)

# Función para agregar actividad a un integrante
def agregar_actividad():
    # Pedimos el ID del integrante (ya debe existir un integrante en la base de datos)
    id_integrante = int(input("ID del integrante: "))
    
    # Pedimos los detalles de la actividad
    tipo_actividad = input("Tipo de actividad: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de finalización (YYYY-MM-DD): ")

    # Insertamos la actividad en la tabla de actividades
    cursor.execute('''
        INSERT INTO actividades (ID_integrante, tipo_actividad, fecha_inicio, fecha_fin)
        VALUES (?, ?, ?, ?)
    ''', (id_integrante, tipo_actividad, fecha_inicio, fecha_fin))

    conn.commit()
    print("Actividad agregada correctamente.")

def listar_actividad():
    cursor.execute('SELECT * FROM actividades')
    actividades = cursor.fetchall()
    for actividades in actividades:
        print(actividades)

# Menú principal
def mostrar_menu():
    while True:
        print("\n--- Menú de Administración de Club ---")
        print("1. Ingresar datos")
        print("2. Consultar datos")
        print("3. Eliminar datos")
        print("4. Ordenar datos")
        print("5. Listar todos los datos")
        print("6. Listar Actividad")
        print("7. Agregar actividad")  
        print("8. Salir") 
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            agregar_integrante()
        elif opcion == 2:
            consultar_integrantes()
        elif opcion == 3:
            eliminar_integrante()
        elif opcion == 4:
            ordenar_integrantes()
        elif opcion == 5:
            consultar_integrantes()
        elif opcion == 6:
            listar_actividad()
        elif opcion == 7:  
            agregar_actividad()
        elif opcion == 8:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el sistema
crear_tablas()
mostrar_menu()

# Cerrar la conexión con la base de datos al salir
conn.close()
