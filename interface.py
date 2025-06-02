from database import agregar_empleado

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar empleado")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            name = input("Nombre: ")
            fecha = input("Fecha de nacimiento: ")
            sexo = input("Sexo: ")
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            agregar_empleado(name, fecha, sexo, usuario, contrasena)
            print("Empleado agregado exitosamente.")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
