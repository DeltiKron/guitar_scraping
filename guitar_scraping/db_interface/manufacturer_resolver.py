from guitar_scraping.config import Session
from guitar_scraping.db_interface.data_models import ManufacturerInfo

session = Session()

def get_manufacturer_id(manufacturer):
    result = [*session.query(ManufacturerInfo.id).filter_by(name=manufacturer)]
    if not result:
        session.add(ManufacturerInfo(name=manufacturer))
        result = [*session.query(ManufacturerInfo.id).filter_by(name=manufacturer)]
    session.commit()
    return result[0][0]

