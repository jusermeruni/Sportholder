from sqlalchemy import Column, Integer, String

# Importamos la clase Base desde el archivo database.py
from database import Base

# Definición de la clase Usuario, que hereda de Base
class Usuario(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'usuarios'

    # Definición de las columnas de la tabla
    # Se especifica el tipo de dato y otras propiedades como la clave primaria, índices, etc.
    cedula = Column(Integer, primary_key=True, index=True)
    contraseña = Column(String(15))
    nombre = Column(String(30))
    apellido = Column(String(30))
    fechaNacimiento = Column(String(15))
    correo = Column(String(30), index=True, unique=True)  # Índice y unicidad en la columna 'correo'
    telefono = Column(Integer, unique=True)  # Unicidad en la columna 'telefono'
    idDocumento = Column(String(5))
    idGenero = Column(String(5))
    idTipo = Column(Integer)
