from abc import ABC, abstractmethod

class Persona:
    def __init__(self, name: str, fecha: str, sexo: str):
        self.name = name
        self.fecha = fecha
        self.sexo = sexo

class Empleado(Persona):
    def __init__(self, name: str, fecha: str, sexo: str, usuario: str, contrasena: str):
        super().__init__(name, fecha, sexo)
        self.usuario = usuario
        self.contrasena = contrasena

class Cliente(Persona):
    def __init__(self, name: str, fecha: str, sexo: str, contrato: str, cantidad_habitaciones: int, habitacion: int):
        super().__init__(name, fecha, sexo)
        self.contrato = contrato
        self.cantidad_habitaciones = cantidad_habitaciones
        self.habitacion = habitacion

class ClienteVip(Cliente):
    def __init__(self, name: str, fecha: str, sexo: str, contrato: str, cantidad_habitaciones: int, habitacion: int, id_vip: str, beneficios_vip: str):
        super().__init__(name, fecha, sexo, contrato, cantidad_habitaciones, habitacion)
        self.id_vip = id_vip
        self.beneficios_vip = beneficios_vip

class ServicioCliente:
    def __init__(self, id_servicio: int, nombre_servicio: str, descripcion: str, costo: float, disponibilidad: bool):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.descripcion = descripcion
        self.costo = costo
        self.disponibilidad = disponibilidad

class Reserva:
    def __init__(self, fecha_inicio: str, fecha_fin: str, numero_lote: int, estado: bool, cliente: Cliente):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.numero_lote = numero_lote
        self.estado = estado
        self.cliente = cliente

class Espacio(ABC):
    def __init__(self, numero_lote: int, precio: float, estado: bool):
        self.numero_lote = numero_lote
        self.precio = precio
        self.estado = estado

    @abstractmethod
    def liberarespacio(self):
        pass

    def reservarespacio(self):
        self.estado = False

class Habitacion(Espacio):
    def __init__(self, numero_lote: int, precio: float, estado: bool, categoria: str, tipo: str, piso: int):
        super().__init__(numero_lote, precio, estado)
        self.categoria = categoria
        self.tipo = tipo
        self.piso = piso

    def liberarespacio(self):
        self.estado = True

class Parqueamiento(Espacio):
    def __init__(self, numero_lote: int, precio: float, estado: bool, capacidad: int, ubicacion: str):
        super().__init__(numero_lote, precio, estado)
        self.capacidad = capacidad
        self.ubicacion = ubicacion

    def liberarespacio(self):
        self.estado = True

class Pago:
    def __init__(self, id_pago: int, fecha_pago: str, monto: float, numero_tarjeta: str):
        self.id_pago = id_pago
        self.fecha_pago = fecha_pago
        self.monto = monto
        self.numero_tarjeta = numero_tarjeta
