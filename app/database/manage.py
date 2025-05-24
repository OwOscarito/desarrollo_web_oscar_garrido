from sqlalchemy import text
from db import Base, engine, SessionLocal, get_count, Comuna, Region
from argparse import ArgumentParser


def execute_sql_file(session, file: str):
    with open(file, "r") as sql_file:

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
                    except:
                        print("Error executing SQL command:", sql_command)
                    # Finally, clear command string
                    finally:
                        sql_command = ""


def init_tables():
    session = SessionLocal()
    execute_sql_file(session, "app/database/tarea2.sql")
    execute_sql_file(session, "app/database/tabla-comentario.sql")
    session.commit()


def init_region_comuna():
    session = SessionLocal()
    execute_sql_file(session, "app/database/region-comuna.sql")
    session.commit()


def drop_db():
    # Create a new session
    session = SessionLocal()

    # Drop all tables
    Base.metadata.drop_all(engine)
    # Close the session
    session.close()

    print("¡Tablas eliminadas!")


def init_db():
    REGION_COUNT = 16
    COMUNA_COUNT = 345

    init_tables()
    print("¡Tablas creadas!")

    if get_count(Comuna) < REGION_COUNT or get_count(Region) < COMUNA_COUNT:
        init_region_comuna()
        print("¡Regiones y comunas inicializadas!")


if __name__ == "__main__":
    parser = ArgumentParser(description="Initialize or drop the database.")
    parser.add_argument(
        "command",
        help="init or drop",
    )

    args = parser.parse_args()

    match args.command:
        case "drop":
            drop_db()
        case "init":
            init_db()
        case _:
            print("Invalid command. Use 'init' or 'drop'.")
            exit(1)
