from glob import glob
import pandas as pd
import datetime
import locale
import os

def get_date(date_string):
    locale.setlocale(locale.LC_ALL, '')
    time = datetime.datetime.strptime(date_string,'%B %Y')
    date = time.date()
    return date

def get_data(filename):
    df = pd.read_csv(filename,index_col='artikelnummer')
    df.category = os.path.basename(filename)
    return df

def clean_data(df):
    df = df.loc[~df.index.duplicated(keep='first')]

    # convert market_release to date
    start_date = df['erhältlich_seit'].dropna()
    start_date_dt = start_date.apply(get_date)
    df['erhältlich_seit'] = start_date_dt

    # convert numerical columns
    numerical_columns = ['bünde', 'preis', 'sattelbreite_in_mm']
    for c in numerical_columns:
        col = df[c]
        try:
            col = pd.to_numeric(col)
        except:
            col = col.apply(str)
            col = col.str.extract(r'(\d+[,\.]*\d*)').iloc[0]
            col = col.str.replace(',','.')
            col = pd.to_numeric(col)
        df[c]=col

    # convert categorical columns
    categorical_columns = ['boden_und_zargen','decke','griffbrett','hersteller']
    for c in categorical_columns:
        col = df[c]
        col = col.astype('category')
        df[c]=col

    # convert boolean columns
    boolean_columns = ['cutaway','inkl_gigbag','koffer','tonabnehmer']
    as_bool = df[boolean_columns].apply(lambda x: pd.Series.map(x,{'Nein':False,'Ja':True}), axis = 1)
    as_bool=as_bool.fillna(False)
    df[boolean_columns] = as_bool

    # drop columns with too few entries
    threshold = len(df)*.5
    df = df.dropna(axis=1, thresh=threshold)
    return df

def get_cleaned_guitar_data():
    files = glob('*.csv')
    df = get_data(files[0])
    for f in files[1:]:
        df = df.append(get_data(f))

    cleaned = clean_data(df)
    return cleaned