import sqlite3

def crear_tablas():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            fecha TEXT,
            sexo TEXT,
            usuario TEXT,
            contrasena TEXT
        )
    ''')

    conn.commit()
    conn.close()

def agregar_empleado(name, fecha, sexo, usuario, contrasena):
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO empleados (name, fecha, sexo, usuario, contrasena)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, fecha, sexo, usuario, contrasena))

    conn.commit()
    conn.close()
