import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Conexión a la base de datos SQL Server
def conectar_bd():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=HotelDB;'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        messagebox.showerror("Error de conexión", str(e))
        return None

# Ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Hotel")
root.geometry("600x400")

# Variables de entrada
nombre_var = tk.StringVar()
nacimiento_var = tk.StringVar()
sexo_var = tk.StringVar()
contrato_var = tk.StringVar()
habitaciones_var = tk.IntVar()
habitacion_var = tk.IntVar()

# Función para simular registro de cliente
def registrar_cliente():
    nombre = nombre_var.get()
    nacimiento = nacimiento_var.get()
    sexo = sexo_var.get()
    contrato = contrato_var.get()
    habitaciones = habitaciones_var.get()
    habitacion = habitacion_var.get()

    if nombre and nacimiento and sexo and contrato and habitaciones and habitacion:
        conn = conectar_bd()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Clientes (Nombre, FechaNacimiento, Sexo, Contrato, CantidadHabitaciones, HabitacionAsignada)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, nombre, nacimiento, sexo, contrato, habitaciones, habitacion)
                conn.commit()
                conn.close()
                messagebox.showinfo("Registro exitoso", f"Cliente {nombre} registrado con éxito.")
            except Exception as e:
                messagebox.showerror("Error al registrar", str(e))
    else:
        messagebox.showwarning("Datos incompletos", "Por favor complete todos los campos.")
        
# Etiquetas y campos de entrada
ttk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=nombre_var).grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Fecha de nacimiento:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=nacimiento_var).grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Sexo:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=sexo_var).grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Contrato:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=contrato_var).grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Cantidad de habitaciones:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=habitaciones_var).grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text="Habitación asignada:").grid(row=5, column=0, padx=10, pady=5, sticky='w')
ttk.Entry(root, textvariable=habitacion_var).grid(row=5, column=1, padx=10, pady=5)

# Botón de registro
ttk.Button(root, text="Registrar Cliente", command=registrar_cliente).grid(row=6, column=1, pady=20)

# Iniciar la interfaz
root.mainloop()