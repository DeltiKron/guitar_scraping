from clean_data import get_cleaned_df
df = get_cleaned_df()
from clean_data import get_data
df = get_data()
from clean_data import get_cleaned_guitar_data
get_cleaned_guitar_data?
df = get_cleaned_guitar_data()
df
df.info()
df.columns
modell
df.bauweise.value
df.bauweise.value_counts()
df.columns
df.boden_und_zargen.value_counts()
df.decke
df.groupby("modell").apply(lmbda x: x[0])
df.groupby("modell").apply(lambda x: x[0])
group0 = next(df.groupby("modell"))
group0 = df.groupby("modell")
group0
type(group0)
dir(group0)
group0.first??
group0.first()
guitars_only = df.groupby("modell").first()
guitars_only
guitars_only.bauweise.value_counts
guitars_only.bauweise.value_counts.info()
guitars_only.isnull.sum()
guitars_only.isnull().sum()
guitars_only.isnull().mean()
hersteller = df.hersteller.unique()
hersteller
len(hersteller)
hersteller_map = {h:i for h,i in enumerate hersteller}
hersteller_map = {h:i for h,i in enumerate(hersteller)}
hersteller_map
hersteller = df.hersteller.value_counts()
hersteller
hersteller = df.hersteller.value_counts().index
hersteller
hersteller_map = {h:i for h,i in enumerate(hersteller)}
hersteller_map
hersteller_df = pd.DataFrame(hersteller)
import pandas as pd
hersteller_df = pd.DataFrame(hersteller)
hersteller_df
hersteller_df.reset_index(inplace=True)
hersteller_df
hersteller.columns = ["id","name"]
hersteller
import sqlalchemy as sa
sa.create_engine
engine = sa.create_engine("sqlite:///guitar_prices.db")
pd.read_sql("SELECT * from guitars")
pd.read_sql("SELECT * from guitars",engine)
pd.read_sql("SELECT * from prices",engine)
pd.to_sql?
hersteller.to_sql?
type(hersteller)
type(hersteller_df)
hersteller_df
hersteller_df.to_sql?
hersteller_df.to_sql("hersteller",engine,index=False)
pd.read_sql("SELECT * from hersteller",engine)
engine.execute()
engine.execute(".tables")
engine.execute("select * from hersteller")
_.fetchall()
engine.url
pwd ///guitar_prices.db
ls /
pwd
ls
engine = sa.create_engine("sqlite:////dat/schaffer/projects/guitar_scraping/guitar_scraping/guitar_prices.db")
engine.table_names()
who engine
dir(engine)
pd.DataFrame({i:i**2 for i in range(10**8)}).to_sql("hersteller",engine,index=False)
pd.DataFrame({i:i**2 for i in range(10**5)}).to_sql("squares",engine,index=False)
pd.DataFrame({i:f"{i**2 }"for i in range(10**5)}).to_sql("squares",engine,index=False)
pd.DataFrame({str(i):f"{i**2 }" for i in range(10**5)}).to_sql("squares",engine,index=False)
pd.DataFrame(dict(one = range(1,20001,2),two = range(0,20000,2) )).to_sql("squares",engine,index=False)
sa.create_engine?
engine = sa.create_engine("sqlite:///testing.db")
pd.DataFrame({str(i):f"{i**2 }" for i in range(10**5)}).to_sql("squares",engine,index=False)
pd.DataFrame(dict(one = range(1,20001,2),two = range(0,20000,2) )).to_sql("squares",engine,index=False)
engine = sa.create_engine("sqlite:///guitar_listings.db")
hersteller_df.to_sql("hersteller",engine,index=False)
hersteller_df.to_sql("hersteller",engine)
hersteller_df.to_sql("hersteller",engine,if_exists="replace")
hersteller_df.to_sql?
hersteller_df.columns
hersteller_df.columns = ["id", "name" ]
hersteller_df.to_sql("hersteller",engine,if_exists="replace")
hersteller_df.to_sql("hersteller",engine,if_exists="replace",index=False)
hersteller_df
hersteller_map
who
guitars_only
hersteller_map
hersteller_map = {h,i for i, h in hersteller_map.items()}
hersteller_map = {h:i for i, h in hersteller_map.items()}
hersteller_map
guitars_only.hersteller.apply(lambda x: hesteller_map[x] if x in hersteller_map else x)
guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.hersteller_id.value_counts()
guitars_only.info()
guitars_only.erhältlich_seit
pd.to_datetime(guitars_only.erhältlich_seit)
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)
guitars_only
guitars_only.info()
guitars_only.isnull().mean()
guitars_only.reset_index(inplace=True)
guitars_only
guitars_only.info()
guitars_only["holz_boden_zargen"] = guitars_only.boden_und_zargen
guitars_only["cutaway"]= guitars_only.cutaway.astype(bool)
guitars_only["holz_decke"] = guitars_only.decke
guitars_only["tonabnehmer"]= guitars_only.cutaway.astype(bool)
guitars_only["tonabnehmer"]= df.groupby("modell").first().cutaway.astype(bool)
guitars_only.info()
guitars_only.bünde.value_counts()
guitars_only.bünde.value_counts().sort_index()
guitars_only.loc[guitars_only["bünde"] > 25] = 0
guitars_only.bünde.value_counts().sort_index()
guitars_only
guitars_only.loc[guitars_only["bünde"] > 25]
guitars_only.loc[guitars_only["bünde"] == 0 ]
guitars_only.info()
%history
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first()
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x)
guitars_only.info()
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)guitars_only.reset_index(inplace=True
guitars_only = df.groupby("modell").first() 
guitars_only["hersteller_id"] = guitars_only.hersteller.apply(lambda x: hersteller_map[x] if x in hersteller_map else x) 
guitars_only.info() 
guitars_only["erhaeltlich_seit"] = pd.to_datetime(guitars_only.erhältlich_seit)
guitars_only.info()
guitars_only.loc[guitars_only["bünde"] > 25].bünde = 0
guitars_only.loc[guitars_only["bünde"] > 25, "bünde"] = 0
guitars_only.bünde
import numpy as np
guitars_only.bünde.replace(0,np.nan)
guitars_only.bünde.replace(0,np.nan,inplace=True)
guitars_only.info()
guitars_only.buende = guitars_only.bünde
guitars_only["buende"] = guitars_only.bünde
guitars_only.info()
guitars_only.isnull.sum()
guitars_only.isnull().sum()
guitars_only.columns
to_db = guitars_only[[]]
guitars_only["holz_decke"] = guitars_only.decke
guitars_only["holz_boden_zargen"] = guitars_only.boden_und_zargen
guitars_only.columns
to_db = guitars_only[['bauweise', 'cutaway', 'farbe', 'griffbrett', 'inkl_gigbag',
       'koffer', 'tonabnehmer', 'verkaufsrang', 'hersteller_id', 'erhaeltlich_seit', 'buende', 'holz_decke',
       'holz_boden_zargen']].reset_index()
to_db
to_db.sort_values("erhaeltlich_seit")
to_db.sort_values("erhaeltlich_seit",ascending=False)
to_db.sort_values("erhaeltlich_seit",ascending=False).to_sql("gitarren", engine, if_exists="replace", index=False)
pd.read_sql(query, engine)
query = """SELECT modell, erhaeltlich_seit, farbe, hersteller from guitars join hersteller on hersteller.id = gitarren.hersteller_id """
pd.read_sql(query, engine)
query = """SELECT modell, erhaeltlich_seit, farbe, hersteller from gitarren join hersteller on hersteller.id = gitarren.hersteller_id """
pd.read_sql(query, engine)
query = """SELECT modell, erhaeltlich_seit, farbe, name from gitarren join hersteller on hersteller.id = gitarren.hersteller_id """
pd.read_sql(query, engine)
query = """SELECT modell, erhaeltlich_seit, farbe, name as hersteller from gitarren join hersteller on hersteller.id = gitarren.hersteller_id """
pd.read_sql(query, engine)
table = pd.read_sql(query, engine)
table
table.erhaeltlich_seit
table.erhaeltlich_seit.value_counts()
pd.to_datetime(table.erhaeltlich_seit.value_counts())
pd.to_datetime(table.erhaeltlich_seit)
since = pd.to_datetime(table.erhaeltlich_seit)
import seaborn as sns
sns.distplot(since)
ll
df
df.columns
df.reset_index
df = df.reset_index()
df["artikelnummer","date","preis","verkaufsrang"]
df[["artikelnummer","date","preis","verkaufsrang"]]
prices = df[["artikelnummer","date","preis","verkaufsrang"]]
to_db
df[["artikelnummer","date","preis","verkaufsrang"]]
df[["artikelnummer","date","preis","verkaufsrang","modell"]]
sales = df[["artikelnummer","date","preis","verkaufsrang","modell"]]
guitar_names = sales[["modell", "artikelnummer"]].drop_duplicates()
guitar_names
guitar_names.dropna(subset="artikelnummer")
guitar_names.dropna(subset=["artikelnummer"])
guitar_names = guitar_names.dropna(subset=["artikelnummer"])
to_db.join(guitar_names, on="modell")
guitar_names
to_db.info()
to_db.join(guitar_names, on="modell")
to_db.join(guitar_names, on="modell",how="left")
to_db.join(guitar_names, left_on="modell",right_on,how="left")
to_db.merge(guitar_names, left_on="modell",right_on,how="left")
to_db.merge(guitar_names, left_on="modell",right_on="modell" ,how="left")
to_db.shape
to_db = to_db.merge(guitar_names, left_on="modell",right_on="modell" ,how="left")
to_db.sort_values("erhaeltlich_seit",ascending=False).to_sql("gitarren", engine, if_exists="replace", index=False)
sales.columns
sales = sales[['artikelnummer', 'date', 'preis', 'verkaufsrang']]
sales
sales.info()
sales.groupby(["artikelnummer","date"]).apply(lambda x: len(x))
sales.groupby(["artikelnummer","date"]).apply(lambda x: len(x)).value_counts()
sales
sales.to_sql("sales", engine, if_exists="replace", index=False)
pd.read_sql("SELECT artikelnummer, preis, date, verkaufsrang from sales", engine)
df = pd.read_sql("SELECT artikelnummer, preis, date, verkaufsrang from sales", engine)
df
df.artikelnummer.value_counts()
df.artikelnummer.value_counts()[:10]
df.artikelnummer.value_counts().iloc[:10]
top_10 = df.artikelnummer.value_counts().iloc[:10].index
for art in artikelnummer:
    res = df.query(f"artikelnummer=='{art}'")
    dates = res.date
    preis = res.preis
    plt.plot(dates,preis, label=f"{art}")
for art in top_10:
    res = df.query(f"artikelnummer=='{art}'")
    dates = res.date
    preis = res.preis
    plt.plot(dates,preis, label=f"{art}")
import matplotlib.pyplot as plt
for art in top_10:
    res = df.query(f"artikelnummer=='{art}'")
    dates = res.date
    preis = res.preis
    plt.plot(dates,preis, label=f"{art}")
plt.show()
for art in top_10:
    res = df.query(f"artikelnummer=='{art}'")
    dates = res.date
    preis = res.preis
    plt.scatter(dates,preis, label=f"{art}")
plt.show()
df.filter?
top_df = df[df.artikelnummer.isin(top_10)]
top_df
import seaborn as sns
sns.lineplot(data=df, x="date", y="preis", hue="artikelnummer")
