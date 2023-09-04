from datetime import datetime

import numpy as np
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
    query = session.query(date, ManufacturerInfo.name, sa.func.count(sa.func.distinct(GuitarInfo.artikelnummer))).filter(
        GuitarInfo.artikelnummer == SalesInfo.artikelnummer).filter(
        GuitarInfo.hersteller_id == ManufacturerInfo.id).group_by(date, ManufacturerInfo.name)
    if start_date:
        query = query.filter(SalesInfo.date > start_date)
    if end_date:
        query = query.filter(SalesInfo.date < end_date)
    records = query.all()
    df = pd.DataFrame(records, columns=['date', 'manufacturer', 'count'])
    df.date = pd.to_datetime(df.date)
    df = df.pivot(columns='manufacturer', index='date', values='count')
    return df


def unique_articles_per_manufacturer_over_time(start_date=None, end_date=None):
    session = Session(engine)
    date = sa.func.date(SalesInfo.date)
    query = session.query(date, SalesInfo.artikelnummer, SalesInfo.preis, GuitarInfo.modell,
                          ManufacturerInfo.name).filter(
        GuitarInfo.artikelnummer == SalesInfo.artikelnummer).filter(
        GuitarInfo.hersteller_id == ManufacturerInfo.id)
    if start_date:
        query = query.filter(SalesInfo.date > start_date)
    if end_date:
        query = query.filter(SalesInfo.date < end_date)
    records = query.all()
    df = pd.DataFrame(records, columns=['date', 'article_number', 'price', 'model_name', 'manufacturer'])

    manufacturers = df.manufacturer.unique()
    manufacturer_count = {manufacturer: set() for manufacturer in manufacturers}
    days = df.date.unique()

    array_res = np.zeros((len(days), len(manufacturer_count)))

    day = df.date[0]
    i = 0
    for row_record in df.sort_values('date').iterrows():
        index, row = row_record
        date = row['date']
        # add data entry if on new day
        if day is not None and date != day:
            array_res[i, :] = np.array([len(manufacturer_count[m]) for m in manufacturers])
            day = date
            i += 1

        manufacturer = row['manufacturer']
        article = row['article_number']
        manufacturer_count[manufacturer].add(article)

    df_res = pd.DataFrame(array_res, columns=manufacturers, index=sorted(days))
    return df_res

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

def articles_mean_price():
    session = Session(engine)
    query = session.query(sa.func.avg(SalesInfo.preis).label('avg_price'),  GuitarInfo, ManufacturerInfo, SalesInfo).filter(
        GuitarInfo.artikelnummer == SalesInfo.artikelnummer).filter(
        GuitarInfo.hersteller_id == ManufacturerInfo.id).group_by(GuitarInfo.artikelnummer)
    df = pd.read_sql(query.statement, query.session.bind)
    return df

def seasonality_base_data():
    session = Session(engine)
    query ="select artikelnummer, date, preis from sales where (artikelnummer, strftime('%Y',date)) in (select artikelnummer, strftime('%Y', date) as year from sales group by artikelnummer, year having count(artikelnummer > 360) order by artikelnummer asc , year asc);"
    df = pd.read_sql(query, engine)
    df.date = pd.to_datetime(df.date)
    return df

if __name__ == '__main__':
    day_data(datetime(2020,5,31).date())
    # print(sales_availability())
    print(daywise_manufacturer_count(start_date=datetime(2020, 10, 10), end_date=datetime(2020, 11, 15)))
