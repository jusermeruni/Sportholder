from pydantic import BaseModel

class UsuarioDate(BaseModel):
    contraseña: str  # Añadir anotación de tipo
    nombre: str
    apellido: str
    fechaNacimiento: str
    correo: str
    telefono: int
    idDocumento: str
    idGenero: str
    idTipo: int

class UsuarioCedula(UsuarioDate):
    cedula: int  # Añadir anotación de tipo
