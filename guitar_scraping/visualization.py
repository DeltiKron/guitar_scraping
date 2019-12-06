import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from clean_data import get_cleaned_guitar_data


def setup_style():
    sns.set_style('darkgrid')


class Guitar_Visualization():
    def __init__(self):
        """
        Class for visual EDA of the Thomann guitar dataset.
        """
        self.data = get_cleaned_guitar_data()
        setup_style()

    def price_histogram(self):
        df = self.data
        fig, ax = plt.subplots()
        df.preis.hist(bins=50, ax=ax)
        plt.title('Price of Steel String Guitars')
        ax.set_xlabel('price/€')
        ax.set_ylabel('count')
        return fig

    def price_by_brand(self):
        df = self.data
        fig, ax = plt.subplots()

        # get top 10 manufacturers and filter data
        counts = df.groupby('hersteller')['modell'].count()
        top_manufacturers = counts.sort_values(ascending=False).iloc[:10].index.tolist()
        filtered_data = df[df.hersteller.map(lambda x: x in top_manufacturers)].copy()
        filtered_data.hersteller = filtered_data.hersteller.astype(str)

        ax = sns.stripplot(x='hersteller', y='preis', data=filtered_data)
        plt.xticks(rotation=90)
        plt.tight_layout()
        return ax



def change_plot(total_data_frame):
    """Make a plot of the price of the most strongly varying guitars over time."""
    variation = total_data_frame.groupby("artikelnummer")["preis"].std()
    changed = variation[ variation > 0]
    art_nummern = changed.index
    only_with_changes = total_data_frame.loc[(art_nummern,slice(None))]
    largest_changes = only_with_changes.groupby("artikelnummer")['preis'].std().sort_values().tail(20).index
    changers = total_data_frame.loc[(largest_changes,slice(None))]
    changers = changers.reset_index()
    changers['date'] = pd.to_datetime(changers.date).dt.date
    data = changers[['artikelnummer', 'date', 'modell','preis','hersteller']]
    sns.lineplot(x='date',y='preis',hue='modell',data=data)


if __name__ == '__main__':
    gv = Guitar_Visualization()
    print(gv.data.columns)
    fig = gv.price_by_brand()
    plt.show()
