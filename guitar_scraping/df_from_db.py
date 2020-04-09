import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///guitar_scraping.db")
import pandas as pd
query = "SELECT hersteller_name, modell, AVG(preis) from gitaren join hersteller on gitarren.hersteller_id=hersteller.id join preis on gitarren.artikelnummer=preis.artikelnummer GROUP BY modell"
pd.read_sql(query,engine)
df = pd.read_sql(query,engine)
query = "SELECT hersteller_name, modell, AVG(preis) from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join preis on gitarren.artikelnummer=preis.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
engine.execute(".tables")
engine.execute("select * from tables")
engine.table_names()
engine = sqlalchemy.create_engine("sqlite:///guitar_scraping.db")
engine.table_names()
engine = sqlalchemy.create_engine("sqlite:///guitar_listings.db")
df = pd.read_sql(query,engine)
query = "SELECT hersteller_name, modell, AVG(preis) from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=preis.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
query = "SELECT hersteller.name, modell, AVG(preis) from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=preis.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
query = "SELECT hersteller.name, modell, AVG(preis) from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=sales.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
df
df.preis.hist()
df
df.columns
query = "SELECT hersteller.name, modell, AVG(preis) as preis from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=sales.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
df
df.preis.hist()
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(df.preis, bins=20)
plt.show()
query = "SELECT hersteller.name, modell, AVG(preis) as preis from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=sales.artikelnummer GROUP BY modell WHERE preis <600"
df.preis.hist()
sns.distplot(df.preis, bins=20)
plt.show()
sns.distplot(df.preis, bins=20)
plt.show()
df = pd.read_sql(query,engine)
query = "SELECT hersteller.name, modell, AVG(preis) as preis from gitarren join hersteller on gitarren.hersteller_id=hersteller.id join sales on gitarren.artikelnummer=sales.artikelnummer GROUP BY modell"
df = pd.read_sql(query,engine)
sns.distplot(df[200< df.preis < 600].preis, bins=20)
sns.distplot(df[(200< df.preis)&(df.preis < 600)].preis, bins=20)
plt.show()
my_range = df[(200< df.preis)&(df.preis < 600)]
my_range = df[(200< df.preis)&(df.preis < 600)].copy
my_range
my_range.columns
my_range = df[(200< df.preis)&(df.preis < 600)].copy()
my_range.columns
my_range.name
my_range.name.value_counts()
df[df.modell.str.contains(df.name)]
df[df.modell.str.contains("Earth")]
