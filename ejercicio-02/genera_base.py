from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return "Pais: nombre=%s capital=%s continente:%s dial:%s geoname_id:%s itu:%s lenguajes:%s independiente:%s \n" % (
                          self.nombre, 
                          self.capital, 
                          self.continente,
                          self.dial,
                          self.geoname_id,
                          self.itu,
                          self.lenguajes,
                          self.independiente,)
    


Base.metadata.create_all(engine)

