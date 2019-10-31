import datetime
import urllib.request as url
from os.path import basename
from time import sleep

import bs4
from IPython import embed
import pandas as pd

def parse_list_page_for_links(page):
    links = []
    next = page

    while next:
        print(next)
        page_html = url.urlopen(next)
        soup = bs4.BeautifulSoup(page_html, 'html.parser')
        guitars = soup.find_all('a', {'class': 'article-link link'})
        guitar_links = [g.attrs['href'].strip() for g in guitars]
        links += set(guitar_links)

        next_page = soup.find_all('a', {'class': "button next"})
        next = "https://www.thomann.de" + next_page[0]['href'] if next_page else False
    return links


keys = [
    'model',
    'manufacturer',
    'preis',
    'artikelnummer',
    u'sattelbreite_in_mm',
    u'decke',
    u'inkl_gigbag',
    u'farbe',
    u'tonabnehmer',
    u'griffbrett',
    u'bauweise',
    u'cutaway',
    u'boden_und_zargen',
    u'koffer'
]



def get_price(soup):
    """
    Extract price from guitar-info page
    :param soup:  BeautifulSoup instance
    :return: price
    """
    price = soup.find('meta', {'itemprop': 'price'}).attrs['content']
    price = float(price)
    return price


def get_model(soup):
    """
    Extract model name from guitar-info page
    :param soup:  BeautifulSoup instance
    :return: model name
    """
    name_cont = soup.find(class_='rs-prod-headline')
    model = name_cont.find(itemprop='name')
    if model:
        return model.text.strip()


def get_manufacturer(soup):
    """
    Extract manufacturer from guitar-info page
    :param soup:  BeautifulSoup instance
    :return: manufacturer, string
    """
    man_logo = soup.find(class_='rs-prod-manufacturer-logo')
    manufacturer = man_logo.find('img')['alt']
    return manufacturer


def get_sales_rank(soup):
    """
    Extract sales rank from guitar-info page
    :param soup:  BeautifulSoup instance
    :return: thomann internal sales rank
    """
    ranking = soup.find(class_='ranking')
    rank = ranking.find_all('tr')[-1].find_all('td')[-1].text
    return int(rank)


def clean_key(instring):
    '''reformatting for locale reasons, minor'''
    outstring = instring
    outstring = outstring.replace(' ', '_')
    outstring = outstring.replace('.', '_')
    outstring = outstring.replace('__', '_')
    return outstring


def scrape_guitar(page):
    """Scrape attributes from a guitar info page
    :param page: URL to info page
    :return: dictionary of attributes parsed from page
    """
    with url.urlopen(page) as thepage:
        soup = bs4.BeautifulSoup(thepage, 'html.parser')
        attrs = soup.find('div', {'class': 'rs-prod-keyfeatures'}).find_all('tr')
        attr_dict = {}
        for row in attrs:
            key = row.find('th').text.strip().lower()
            val = row.find('td').text.strip()
            attr_dict[clean_key(key)] = val

        info = soup.find('div', {'class': 'info'})
        meta_table = info.find('table', {'class': 'meta-table rs-text'}).find_all('tr')

        for row in meta_table:
            fields = row.find_all('td')
            key = fields[0].text.strip().lower()
            val = fields[1].text.strip()
            attr_dict[clean_key(key)] = val

        price = get_price(soup)
        attr_dict['preis'] = price
        attr_dict['hersteller'] = get_manufacturer(soup)
        attr_dict['verkaufsrang'] = get_sales_rank(soup)

        attr_dict['modell'] = get_model(soup)
    return attr_dict


if __name__ == '__main__':
    landing_pages = [
        'https://www.thomann.de/de/sonstige_westerngitarren.html?pg=1&ls=100',
        'https://www.thomann.de/de/dreadnought_gitarren.html',
        'https://www.thomann.de/de/jumbo_gitarren.html',
        'https://www.thomann.de/de/folk_gitarren.html',
        'https://www.thomann.de/de/sonstige_westerngitarren.html',
    ]
    for landing_page in landing_pages:

        links = parse_list_page_for_links(landing_page)
        links = list(set(links))
        n_links = len(links)
        chunk_size = 100
        chunks = [links[i:min(i + chunk_size, n_links - 1)] for i in range(0, n_links, chunk_size)]
        dicts = []
        for i, chunk in enumerate(chunks):
            for l in chunk:
                print(l)
                try:
                    dicts.append(scrape_guitar(l))
                except:
                    print("error")
                    continue
                sleep(1)

            fn = basename(landing_page).split('.')[0]
            df = pd.DataFrame(dicts)
            df["date"] = datetime.datetime.now()
            full_fn = fn + f"_chunk_{i:03d}.csv"
            df.to_csv(full_fn)
