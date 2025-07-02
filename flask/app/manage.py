from sqlalchemy import text
from database import db
from argparse import ArgumentParser
import datetime as dt
import random as rd
import pathlib
import shutil

def execute_sql_file(session, file: str):
    with open(file, "r", encoding="utf-8") as sql_file:

        sql_command = ""
    
        for line in sql_file:
            # Ignore commented lines
            if not line.startswith("--") and line.strip("\n"):
                # Append line to the command string
                sql_command += line.strip("\n")

                # If the command string ends with ';', it is a full statement
                if sql_command.endswith(";"):
                    # Try to execute statement and commit it
                    try:
                        session.execute(text(sql_command))
                        session.commit()
                    # Assert in case of error
                    except Exception as e:
                        print(f"Error {e} executing SQL command: {sql_command}")
                    # Finally, clear command string
                    finally:
                        sql_command = ""

def init_tables():
    session = db.SessionLocal()
    execute_sql_file(session, "app/database/tarea2.sql")
    execute_sql_file(session, "app/database/tabla-comentario.sql")
    session.commit()


def init_region_comuna():
    session = db.SessionLocal()
    execute_sql_file(session, "app/database/region-comuna.sql")
    session.commit()


def drop_db():
    # Create a new session
    session = db.SessionLocal()

    # Drop all tables
    db.Base.metadata.drop_all(db.engine)
    # Close the session
    session.close()

    print("¡Tablas eliminadas!")


def init_db():
    REGION_COUNT = 16
    COMUNA_COUNT = 345


    init_tables()
    print("¡Tablas creadas!")

    if db.get_count(db.Comuna) < REGION_COUNT or db.get_count(db.Region) < COMUNA_COUNT:
        init_region_comuna()
        print("¡Regiones y comunas inicializadas!")

class FakeFileStorage():
    def __init__(self, path: pathlib.Path):
        self.filename = path.name

def example_activity():
    ex_img_path = pathlib.Path("app/static/example/ex1.jpg")
    ex_img = FakeFileStorage(ex_img_path)
    
    base_path, _ = db.create_activity(
        comuna_id=130202,
        sector="Sector de ejemplo",
        nombre="Organizador de ejemplo", 
        email="ejemplo@mail.com",
        tema="otro",
        glosa_otro="Ejemplo", 
        descripcion="Descripción de la actividad de ejemplo", 
        dia_hora_inicio=dt.datetime.now() + dt.timedelta(days=1),
        uploads_folder="uploads",
        fotos=[ex_img],
    )
    
    activity_id = int(base_path.split("/")[-1])
    print(f"Actividad de ejemplo creada con ID: {activity_id}")

    static_path = pathlib.Path("app/static")
    new_path = static_path/base_path
    new_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(ex_img_path, new_path)

    return activity_id

def example_comment(activity_id):
    db.add_comment(
        actividad_id=activity_id,
        nombre=f"Usuario {rd.randint(1, 1000)}",
        texto="Comentario de ejemplo",
        fecha=dt.datetime.now(),
    )
    print("¡Datos de ejemplo añadidos!")

def example_db():
    act_id = example_activity()
    example_comment(act_id)  # Assuming the example activity has ID 1

if __name__ == "__main__":
    parser = ArgumentParser(description="Initialize or drop the database.")
    parser.add_argument(
        "-i", "--init" ,
        help="init",
        action='store_true'
    )
    parser.add_argument(
        "-a", "--activity" ,
        help="example activity",
        action='store_true'
    )
    parser.add_argument(
        "-c", "--comment" ,
        help="example comment",
        type=int,
    )
    parser.add_argument(
        "-d", "--drop" ,
        help="drop",
        action='store_true'
    )

    args = parser.parse_args()

    if args.init:
        init_db()
    if args.drop:
        drop_db()
    if args.activity:
        act_id = example_activity()
    if args.comment:
        example_comment(int(args.comment))
    