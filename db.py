from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:ospitia200@localhost:5432/agenda'

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion establecida con la BD")
    else:
        print("Error en la conexion")
    print("Soy s: ", s)
    return s