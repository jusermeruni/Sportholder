# Importaciones necesarias de SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_NAME= os.getenv('DB_NAME')
DB_HOST= os.getenv('DB_HOST')
DB_PASSWORD= os.getenv('DB_PASSWORD')
DB_DIALECT= os.getenv('DB_DIALECT')
DB_USER= os.getenv('DB_USER')

URL_DATABASE = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER,DB_PASSWORD, DB_HOST, DB_NAME)

# Creación del motor de la base de datos
engine = create_engine(URL_DATABASE)

# Configuración de la clase de fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creación de la clase base para el mapeo de objetos a la base de datos
Base = declarative_base()