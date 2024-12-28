import datetime
import locale
import os
from glob import glob
from os.path import join, dirname

import numpy as np
import pandas as pd
from guitar_scraping.db_interface.manufacturer_resolver import get_manufacturer_id
from tqdm import tqdm


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
    df['date'] = pd.to_datetime(df['date'])
    df['artikelnummer'] = pd.to_numeric(df['artikelnummer'])
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


def get_cleaned_guitar_data(pattern=None):
    pattern = pattern or join(dirname(__file__), '../data/*/*.csv')
    files = glob(pattern)
    df = get_data(files[0])
    progress_bar = tqdm(files[1:])
    for f in progress_bar:
        progress_bar.set_description(f)
        try:
            df = df.append(get_data(f))
        except KeyError as ke:
            print(f'error in {f}')
            print(ke)

    cleaned = clean_data(df)
    return cleaned


def get_guitars(pattern=None):
    df = get_cleaned_guitar_data(pattern)
    df.reset_index(inplace=True)
    # Process guitar model data
    df["hersteller_id"] = df.hersteller.apply(get_manufacturer_id)
    df["erhaeltlich_seit"] = pd.to_datetime(df.erhältlich_seit)
    df["holz_boden_zargen"] = df.boden_und_zargen
    df["cutaway"] = df.cutaway.astype(bool)
    df["holz_decke"] = df.decke
    df["tonabnehmer"] = df.cutaway.astype(bool)
    df["tonabnehmer"] = df.groupby("modell").first().cutaway.astype(bool)
    df.loc[df["bünde"] > 25].bünde = 0
    df.bünde.replace(0, np.nan, inplace=True)
    df.bünde.value_counts().sort_index()
    df["erhaeltlich_seit"] = pd.to_datetime(df.erhältlich_seit)
    df["buende"] = df.bünde
    to_db = df[['artikelnummer', 'bauweise', 'cutaway', 'farbe', 'griffbrett', 'inkl_gigbag',
                'koffer', 'tonabnehmer', 'verkaufsrang', 'hersteller_id', 'erhaeltlich_seit', 'buende',
                'holz_decke', 'modell',
                'holz_boden_zargen']].copy()
    to_db.sort_values("erhaeltlich_seit", ascending=False, inplace=True)
    return to_db


def get_sales(pattern=None):
    df = get_cleaned_guitar_data(pattern)
    df.reset_index(inplace=True)
    sales = df[['artikelnummer', 'date', 'preis', 'verkaufsrang']].copy()
    return sales
