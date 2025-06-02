from abc import ABC, abstractmethod
class Persona:
    def __init__(self, name: str, nacimiento: str, sexo: str):
        self.name = name
        self.nacimiento = edad
        self.sexo = sexo
class Empleado(Persona):
    def __init__(self , idEmpleado: int, usuarioSistema: str, contraseña: str):
        super().__init__(self, name, nacimiento, sexo )
        self.idEmpleado = idempleado
        self.usuarioSistema = usuarioSistema
        self.__contraseña = contraseña
class Cliente(Persona):
    def __init__(self, contrato: str, canitdad_habitaciones: int, habitacion: int):
        self.contrato = contrato
        self.cantidad_habitaciones = cantidad_habitaciones
        self.habitacion = habitacion
class ClienteVip(Cliente):
    def __init__(self, idVip: str, beneficios_Vip: str):
        self.idVip = idvip
        self.beneficios_Vip = beneficios
class ServicioCliente:
    def __init__(self, idServicio: int, nombre_Servicio: str, descripcion: str, costo: float, disponibilidad: bool):
        self.idServicio = idService
        self.nombre_Servicio = nameService
        self.descripcion = descripcion
        self.costo = costo
        self.disponibilidad = disponibilidad
class Reserva:
    def __init__(self, fecha_inicio: int, fecha_fin: int, numero_lote: int, estado: bool, cliente: str):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.numero_lote = numero_lote
        self.estado = estadoreserva
        self.cliente = nombrecliente
#---Clase abstracta 
class Espacio(ABC):
    def __init__(self, numero_lote: int, precio: float, estado: bool):
        self.numero_lote = lote
        self.precio = precio
        self.estado = estadohabitacion
        @abc.abstractmethod
        def liberarespacio(self):
            pass
        def reservarespacio(self):
            self.estado= False
class Habitacion(Espacio):
    def __init__(self, categoria: str, tipo: str, piso: int):
        super().__init__(numero_lote,precio,estado)
        self.categoria = categoria
        self.tipo = tipohabitacion
        self.piso = pisopornivel
    #---Polimorfismo_método abstracto
    def liberarespacio(self):
        self.estado = True
class Parqueamiento(Espacio):
    def __init__(self, capacidad: int, ubicacion: str):
        self.capacidad = capacidad
        self.ubicacion = ubicacionparqueo
    def liberarespacio(self):
        self.estado = True

#---Clase con inyección de dependencias
class metodoDePago:
    pass
class pago:
    def __init__(self, idPago: int, fecha_pago: int, monto: float, numero_tarjeta, metododepago: metodoDePago):
        self.idPago = pago
        self.fecha_pago = fechapago
        self.monto = montoapagar
        self.metododepago = metodoDePago