from guitar_scraping.config import Session


def add_df_to_db(df, data_model):
    session = Session()
    for index, row in df.iterrows():
        kwargs = dict(row.dropna())
        dataset = data_model(**kwargs)
        session.merge(dataset)
    session.commit()