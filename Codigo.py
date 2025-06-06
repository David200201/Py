class Cliente:
    def __init__(self, nombre, cedula, edad, sexo, contrato, cantidadHabitaciones, habitaciones):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sexo = sexo
        self.contrato = contrato
        self.cantidadHabitaciones = cantidadHabitaciones
        self.habitaciones = habitaciones

class Empleado:
    def __init__(self):
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def consulta(self, identificador):
        resultados = []
        if isinstance(identificador, int):
            resultados = [cliente for cliente in self.clientes if cliente.cedula == identificador]
        elif isinstance(identificador, str):
            resultados = [cliente for cliente in self.clientes if cliente.nombre.lower() == identificador.lower()]
        else:
            print("Dato no encontrado o incorrecto")
        return resultados
    
    def mostrar_clientes(self, clientes):
        for cliente in clientes:
            print(f"Cédula: {cliente.cedula}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Edad: {cliente.edad}")
            print(f"Sexo: {cliente.sexo}")
            print(f"Contrato: {cliente.contrato}")
            print(f"Cantidad de Habitaciones: {cliente.cantidadHabitaciones}")
            print(f"Habitaciones: {cliente.habitaciones}")
            print("-" * 30)

# Ejemplo de uso
x = Empleado()
x.agregar_cliente(Cliente("Juanito Alimaña", 1111111111, 32, "M", "164764009kl", 3, [121, 122, 123]))

ident = input("Ingrese nombre o cédula del cliente a buscar: ")

# Intentamos convertir a int si es posible
try:
    ident = int(ident)
except ValueError:
    pass

resultados = x.consulta(ident)

if resultados:
    x.mostrar_clientes(resultados)
else:
    print("No existe ese cliente.")
