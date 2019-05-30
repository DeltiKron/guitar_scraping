import matplotlib.pyplot as plt
import seaborn as sns

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


if __name__ == '__main__':
    gv = Guitar_Visualization()
    print(gv.data.columns)
    fig = gv.price_by_brand()
    plt.show()
