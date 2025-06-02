CREATE DATABASE HotelBD
CREATE TABLE Clientes (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100),
    FechaNacimiento DATE,
    Sexo NVARCHAR(10),
    Contrato NVARCHAR(50),
    CantidadHabitaciones INT,
    HabitacionAsignada INT
);

-- Muestra la tabla actualizada:
SELECT * FROM Clientes
