import numpy as np
import pandas as pd
import sqlalchemy as sa
from clean_data import get_cleaned_guitar_data


def add_to_db(df, table_name):
    db_df = pd.read_sql(f'select * from {table_name}', _engine)
    new_rows = df[~df.isin(db_df)].dropna(how='all')
    new_rows.to_sql(table_name, _engine, if_exists='append')
    print(f' Wrote {len(new_rows)} new rows to tabel {table_name}')


_engine = sa.create_engine("sqlite:////dat/schaffer/projects/guitar_scraping/guitar_scraping/testing.db")

df = get_cleaned_guitar_data('../data/2020-06-28/*.csv')

# ensure unique guitar names
guitars_only = df.groupby("modell").first()


class ManufacturerIdResolver():
    def __init__(self):
        from_db = pd.read_sql("select name, id from hersteller", _engine)
        self.keys = {row['hersteller']: row['id'] for row in from_db.iterrows()}

    def get_id(self, manufacturer):
        if manufacturer in self.keys.keys():
            return self.keys[manufacturer]
        else:
            new_id = max[self.keys.values()] + 1
            self.keys[manufacturer] = new_id
            return new_id


id_resolver = ManufacturerIdResolver()

# Process manufacturer data
hersteller = df.hersteller.unique()
hersteller_df = pd.DataFrame(hersteller)
hersteller_df.reset_index(inplace=True)
hersteller.columns = ["id", "name"]
hersteller_df.to_sql("hersteller", _engine, index=False, if_exists='replace')

# Process guitar model data
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: id_resolver.get_id(x))
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)
guitars_only.reset_index(inplace=True)
guitars_only["holz_boden_zargen"] = guitars_only.boden_und_zargen
guitars_only["cutaway"] = guitars_only.cutaway.astype(bool)
guitars_only["holz_decke"] = guitars_only.decke
guitars_only["tonabnehmer"] = guitars_only.cutaway.astype(bool)
guitars_only["tonabnehmer"] = df.groupby("modell").first().cutaway.astype(bool)
guitars_only.loc[guitars_only["bünde"] > 25].bünde = 0
guitars_only.bünde.replace(0, np.nan, inplace=True)
guitars_only.bünde.value_counts().sort_index()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)
guitars_only["buende"] = guitars_only.bünde
to_db = guitars_only[['bauweise', 'cutaway', 'farbe', 'griffbrett', 'inkl_gigbag',
                      'koffer', 'tonabnehmer', 'verkaufsrang', 'hersteller_id', 'erhaeltlich_seit', 'buende',
                      'holz_decke', 'modell',
                      'holz_boden_zargen']].reset_index()
to_db.sort_values("erhaeltlich_seit", ascending=False)
to_db.sort_values("erhaeltlich_seit", ascending=False, inplace=True)
to_db.to_sql("gitarren", _engine, if_exists="replace", index=False)

# Process sales Data
df = df.reset_index()
sales = df[["artikelnummer", "date", "preis", "verkaufsrang", "modell"]]
guitar_names = sales[["modell", "artikelnummer"]].drop_duplicates()
guitar_names = guitar_names.dropna(subset=["artikelnummer"])
to_db = to_db.merge(guitar_names, left_on="modell", right_on="modell", how="left")
to_db.sort_values("erhaeltlich_seit", ascending=False).to_sql("gitarren", _engine, if_exists="replace", index=False)

sales = sales[['artikelnummer', 'date', 'preis', 'verkaufsrang']]
sales.groupby(["artikelnummer", "date"]).apply(lambda x: len(x))
sales.groupby(["artikelnummer", "date"]).apply(lambda x: len(x)).value_counts()
sales.to_sql("sales", _engine, if_exists="replace", index=False)


def plot_release_date():
    query = """SELECT modell, erhaeltlich_seit, farbe, name as hersteller from gitarren join hersteller on hersteller.id = gitarren.hersteller_id """

    pd.read_sql(query, _engine)
    table = pd.read_sql(query, _engine)
    since = pd.to_datetime(table.erhaeltlich_seit)

    import seaborn as sns
    sns.distplot(since)
