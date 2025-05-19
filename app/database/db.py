from __future__ import annotations
import enum
from sqlalchemy import create_engine, Column, BigInteger, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os
from werkzeug.utils import secure_filename

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# --- Enums ---


class Tema(enum.Enum):
    música = 0
    deporte = 1
    ciencias = 2
    religión = 3
    política = 4
    tecnología = 5
    juegos = 6
    baile = 7
    comida = 8
    otro = 9

class Contacto(enum.Enum):
    whatsapp = 0
    telegram = 1
    X = 2
    instagram = 3
    tiktok = 4
    otra = 5

# --- Models ---

class Region(Base):
    __tablename__ = "region"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    comuna = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = "comuna"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(BigInteger, ForeignKey("region.id"), nullable=False)

    region = relationship("Region", back_populates="comuna")
    actividad = relationship("Actividad", back_populates="comuna")

class Actividad(Base):
    __tablename__ = "actividad"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    comuna_id = Column(BigInteger, ForeignKey("comuna.id"), nullable=False)
    sector = Column(String(100))
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15))
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime)
    descripcion = Column(String(500))

    comuna = relationship("Comuna", back_populates="actividad")
    actividad_tema = relationship("ActividadTema", back_populates="actividad")
    contactar_por = relationship("ContactarPor", back_populates="actividad")
    foto = relationship("Foto", back_populates="actividad")

class ActividadTema(Base):
    __tablename__ = "actividad_tema"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tema = Column(Enum(Tema), nullable=False)
    glosa_otro = Column(String(15))
    actividad_id = Column(BigInteger, ForeignKey("actividad.id"), nullable=False)
    
    actividad = relationship("Actividad", back_populates="actividad_tema")

class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(Enum(Contacto), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(BigInteger, ForeignKey("actividad.id"), nullable=False)
    
    actividad = relationship("Actividad", back_populates="contactar_por")

class Foto(Base):
    __tablename__ = "foto"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(BigInteger, ForeignKey("actividad.id"), nullable=False)
    
    actividad = relationship("Actividad", back_populates="foto")

# --- Functions ---

def create_activity(
    comuna_id,
    nombre,
    email,
    dia_hora_inicio,
    uploads_folder,
    sector=None,
    celular=None,
    dia_hora_termino=None,
    descripcion=None,
    tema=None,
    glosa_otro=None,
    contactos: list = [],
    fotos: list = [],

):
    session = SessionLocal()
    new_activity = Actividad(
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion,
    )
    session.add(new_activity)
    session.flush()

    if tema:
        new_tema = ActividadTema(
            tema=tema, 
            glosa_otro=glosa_otro,
            actividad_id=new_activity.id
            )
    elif glosa_otro:
        new_tema = ActividadTema(tema=Tema.otro, glosa_otro=glosa_otro)
    else:
        raise ValueError("Como llegamos aca?")
    
    new_contactos = []

    for contacto, id in contactos:
        new_contacto = ContactarPor(
            nombre=contacto,
            identificador=id,
            actividad_id=new_activity.id,
        )
        new_contactos.append(new_contacto)


    new_fotos = []
    base_path = os.path.join(uploads_folder, str(new_activity.id))
    for foto in fotos:
        new_foto = Foto(
            ruta_archivo=base_path,
            nombre_archivo=secure_filename(foto.filename),
            actividad_id=new_activity.id,
        )
        new_fotos.append(new_foto)

    session.add(new_tema)
    for new_contacto in new_contactos:
        session.add(new_contacto)
    for new_foto in new_fotos:
        session.add(new_foto)
    session.commit()
    session.close()

    return {"activity": new_activity, "tema": new_tema, "contactos": new_contactos, "fotos": new_fotos}
            
def get_activities(quantity=1, offset=0):
    session = SessionLocal()
    activities = session.query(Actividad).offset(offset).limit(quantity).all()
    session.close()
    return activities

def get_activity_by_id(id):
    session = SessionLocal()
    activity = session.query(Actividad).filter(Actividad.id == id).first()
    session.close()
    return activity

def get_region_by_id(id):
    session = SessionLocal()
    location = session.query(Region).filter(Region.id == id).first()
    session.close()
    return location

def get_commune_by_id(id):
    session = SessionLocal()
    location = session.query(Comuna).filter(Comuna.id == id).first()
    session.close()
    return location

def get_photos_by_activity_id(id):
    session = SessionLocal()
    photos = session.query(Foto).filter(Foto.actividad_id == id).all()
    session.close()
    return photos

def get_count(table):
    session = SessionLocal()
    count = session.query(table.id).count()
    session.close()
    return count