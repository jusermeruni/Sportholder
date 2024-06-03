from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud
from database import engine, SessionLocal
from schemas import UsuarioDate, UsuarioCedula
from models import Base

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

origin = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods='*',
    allow_headers = ['*']
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return 'buenas buenas'

@app.get('/api/usuarios/', response_model=list[UsuarioCedula])
def get_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db)

@app.get('/api/users/{cedula:int}', response_model=UsuarioCedula)
def get_usuario(cedula, db: Session = Depends(get_db)):
    usuario_by_cedula=crud.get_usuario_by_cedula(db=db, cedula=cedula)
    if usuario_by_cedula:
        return usuario_by_cedula
    raise HTTPException(status_code=404, detail='Usuario no encontrado')

@app.post("/api/usuarios1/", response_model=UsuarioCedula)
def create_usuario(usuario: UsuarioCedula, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_correo(db, correo=usuario.correo)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return crud.create_usuario(db=db, usuario=usuario)