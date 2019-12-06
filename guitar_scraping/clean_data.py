import sys
import datetime
import locale
import os
from glob import glob
from os.path import join
import pandas as pd


def get_date(date_string):
    for loc in ["de_DE", "deu_deu"]:
        try:
            locale.setlocale(locale.LC_ALL, loc)
            break
        except:
            continue
    else:
        raise ValueError("couldn't set locale!")

    time = datetime.datetime.strptime(date_string, '%B %Y')
    date = time.date()
    return date


def get_data(filename):
    df = pd.read_csv(filename)
    df['date'] =pd.to_datetime(df['date'])
    df['artikelnummer'] =pd.to_numeric(df['artikelnummer'])
    df = df.set_index(['artikelnummer', 'date'])
    df.category = os.path.basename(filename)
    return df


def clean_data(df):
    df = df.loc[~df.index.duplicated(keep='first')]

    # convert market_release to date
    if 'erhältlich_seit' in df.columns:
        start_date = df['erhältlich_seit'].dropna()
        start_date_dt = start_date.apply(get_date)
        df['erhältlich_seit'] = start_date_dt

    # convert numerical columns
    numerical_columns = ['bünde', 'preis', 'sattelbreite_in_mm']
    for c in numerical_columns:
        if c not in df.columns:
            continue
        col = df[c]
        try:
            col = pd.to_numeric(col)
        except:
            col = col.apply(str)
            col = col.str.extract(r'(\d+[,\.]*\d*)').iloc[0]
            col = col.str.replace(',', '.')
            col = pd.to_numeric(col)
        df[c] = col

    # convert categorical columns
    categorical_columns = ['boden_und_zargen', 'decke', 'griffbrett', 'hersteller']
    for c in categorical_columns:
        if c not in df.columns:
            continue
        col = df[c]
        col = col.astype('category')
        df[c] = col

    # convert boolean columns
    boolean_columns = ['cutaway', 'inkl_gigbag', 'koffer', 'tonabnehmer']
    for b in boolean_columns:
        if b not in df.columns:
            continue
        as_bool = pd.Series.map(df[b], {'Nein': False, 'Ja': True})
        as_bool = as_bool.fillna(False)
        df[b] = as_bool

    # drop columns with too few entries
    threshold = len(df) * .5
    df = df.dropna(axis=1, thresh=threshold)

    if "Unnamed: 0" in df.columns:
        df = df[df.columns.drop("Unnamed: 0")]
    return df

def get_cleaned_df(filename):
    """Read_csv and clean columns."""
    data_frame = get_data(filename)
    cleaned = clean_data(data_frame)
    return cleaned


def get_cleaned_guitar_data():
    files = glob(join(sys.argv[-1], '*.csv'))
    df = get_data(files[0])
    for f in files[1:]:
        df = df.append(get_data(f))

    cleaned = clean_data(df)
    return cleaned
