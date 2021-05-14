from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Pais 

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()


#Presentar los lenguajes de cada país.
paises = session.query(Pais).all()

for pais in paises:
    print("Pais: %s\t\tLenguajes:%s" % (pais.nombre, pais.lenguajes))
    print("--------------------------------------------------------")