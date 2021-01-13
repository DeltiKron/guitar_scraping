from datetime import datetime

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.orm import Session

from guitar_scraping.db_interface.data_models import SalesInfo, engine, ManufacturerInfo, GuitarInfo


def sales_availability():
    """
    Overview of number of listings per day
    """
    # Get number of entries per date
    session = Session(engine)
    res = session.query(sa.func.date(SalesInfo.date), sa.func.count()).group_by(sa.func.date(SalesInfo.date)).all()

    # Package results to df
    df = pd.DataFrame(res, columns=['date', 'available_listings'])
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date')
    return df


def daywise_manufacturer_count(start_date=None, end_date=None):
    session = Session(engine)
    date = sa.func.date(SalesInfo.date)
    query = session.query(date, ManufacturerInfo.name, sa.func.count('*')).filter(
        GuitarInfo.artikelnummer == SalesInfo.artikelnummer).filter(
        GuitarInfo.hersteller_id == ManufacturerInfo.id).group_by(date, ManufacturerInfo.name)
    if start_date:
        query = query.filter(SalesInfo.date > start_date)
    if end_date:
        query = query.filter(SalesInfo.date < end_date)
    records = query.all()
    df = pd.DataFrame(records, columns=['date', 'manufacturer', 'count'])
    df.date = pd.to_datetime(df.date)
    df=df.pivot(columns='manufacturer', index='date', values='count')
    return df

def day_data(date):
    # Clean input to target only specific day
    if isinstance(date,datetime):
        date = datetime.date()

    session = Session(engine)
    query = session.query(GuitarInfo, ManufacturerInfo, SalesInfo).filter(
        GuitarInfo.artikelnummer == SalesInfo.artikelnummer).filter(
        GuitarInfo.hersteller_id == ManufacturerInfo.id)
    query = query.filter(sa.func.date(SalesInfo.date) == date)
    df = pd.read_sql(query.statement, query.session.bind)
    return df

if __name__ == '__main__':
    day_data(datetime(2020,5,31).date())
    # print(sales_availability())
    print(daywise_manufacturer_count(start_date=datetime(2020, 10, 10), end_date=datetime(2020, 11, 15)))
