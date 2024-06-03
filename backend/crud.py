from sqlalchemy.orm import Session

# Importamos el modelo Usuario desde el archivo models
from models import Usuario
# Importamos el esquema UsuarioDate desde el archivo schemas
from schemas import UsuarioDate

# Función para obtener todos los usuarios
def get_usuarios(db: Session):
    return db.query(Usuario).all()

# Función para obtener un usuario por su cédula
def get_usuario_by_cedula(db: Session, cedula: int):
    return db.query(Usuario).filter(Usuario.cedula == cedula).first()

# Función para obtener un usuario por su correo electrónico
def get_usuario_by_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

# Función para crear un nuevo usuario
def create_usuario(db: Session, usuario: UsuarioDate):
    # Se genera una contraseña falsa para almacenarla en la base de datos
    fake_password = usuario.contraseña + '#fake'
    # Se crea una nueva instancia del modelo Usuario con los datos proporcionados
    new_usuario = Usuario(
        cedula=usuario.cedula,  # Asegúrate de manejar 'cedula' aquí
        contraseña=fake_password,
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        fechaNacimiento=usuario.fechaNacimiento,
        correo=usuario.correo,
        telefono=usuario.telefono,
        idDocumento=usuario.idDocumento,
        idGenero=usuario.idGenero,
        idTipo=usuario.idTipo
    )
    # Se agrega el nuevo usuario a la sesión
    db.add(new_usuario)
    # Se confirman los cambios en la base de datos
    db.commit()
    # Se actualiza la instancia de usuario con los valores generados por la base de datos (como el ID)
    db.refresh(new_usuario)
    # Se retorna el nuevo usuario creado
    return new_usuario