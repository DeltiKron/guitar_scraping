from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL= "sqlite:///"+str(Path(__file__).parent / 'guitar_listings.db')

column_name_translation = dict(
    modell="model",
    bauweise="shape",
    farbe="color",
    griffbrett="wood_fretboard",
    inkl_gigbag="gigbag_included",
    koffer="case_included",
    tonabnehmer="has_pickup",
    verkaufsrang="sales_rank",
    hersteller_id="manufacturer_id",
    erhaeltlich_seit="available_since",
    buende="frets",
    holz_decke="wood_top",
    holz_boden_zargen="wood_back_sides",
    artikelnummer="item_number"
)

# Create engine singleton and associated sessionmaker
engine = create_engine(DB_URL)
Session = sessionmaker()
Session.configure(bind=engine)

