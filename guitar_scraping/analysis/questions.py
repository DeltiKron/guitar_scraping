from datetime import datetime
import sqlite3

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.orm import Session

from guitar_scraping.constants import DB_PATH
from guitar_scraping.db_interface.data_models import GuitarInfo, ManufacturerInfo, SalesInfo, engine


def run_query(query_string, **kwargs):
    con = sqlite3.connect( DB_PATH)
    df = pd.read_sql_query(query_string,con, **kwargs )
    return df


def sales_availability():
    """
    Overview of number of listings per day
    """
    # Get number of entries per date
    run_query('select * from listings_per_day order by day asc')
    # Package results to df
    df.day = pd.to_datetime(df.day)
    df = df.set_index('day')
    return df


def daywise_manufacturer_count(start_date=None, end_date=None):
    con = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f'select * from daywise_manufacturer_count where day >= {start_date:"%Y-%m-%d"} and day < {end_date:"%Y-%m-%d"}',con, parse_dates=['day'], index_col=['day'])
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
    # day_data(datetime(2020,5,31).date())
    # print(sales_availability())
    print(daywise_manufacturer_count(start_date=datetime(2020, 10, 10), end_date=datetime(2020, 11, 15)))
    pass
