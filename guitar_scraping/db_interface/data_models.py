from guitar_scraping.config import DB_URL
from sqlalchemy import String, Boolean, BigInteger, Integer, DateTime, Float
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ManufacturerInfo(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class GuitarInfo(Base):
    __tablename__ = 'guitars'
    modell = Column(String)
    bauweise = Column(String)
    cutaway = Column(Boolean)
    farbe = Column(String)
    griffbrett = Column(String)
    inkl_gigbag = Column(Boolean)
    koffer = Column(Boolean)
    tonabnehmer = Column(Boolean)
    verkaufsrang = Column(BigInteger)
    hersteller_id = Column(Integer)
    erhaeltlich_seit = Column(DateTime)
    buende = Column(Float)
    holz_decke = Column(String)
    holz_boden_zargen = Column(String)
    artikelnummer = Column(Integer, primary_key=True)


class SalesInfo(Base):
    __tablename__ = 'sales'
    artikelnummer = Column(Integer, primary_key=True)
    date = Column(DateTime, primary_key=True)
    preis = Column(Float)
    verkaufsrang = Column(BigInteger)


engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
