import bs4
import urllib.request as url
from IPython import embed
from time import sleep
import pandas as pd


def parse_list_page_for_links(page):
    thepage = url.urlopen(page)
    soup = bs4.BeautifulSoup(thepage, 'html.parser')
    guitars = soup.find_all('a', {'class': 'article-link link'})
    links = [g.attrs['href'].strip() for g in guitars]
    thepage.close()
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


def clean_key(instring):
    outstring = instring
    outstring = outstring.replace(' ', '_')
    outstring = outstring.replace('.', '_')
    outstring = outstring.replace('__', '_')
    return outstring


def get_price(soup):
    price = soup.find('meta', {'itemprop': 'price'}).attrs['content']
    price = float(price)
    return price


def get_model(soup):
    name_cont = soup.find(class_='rs-prod-headline')
    model = name_cont.find(itemprop='name')
    if model:
        return model.text.strip()


def get_manufacturer(soup):
    man_logo = soup.find(class_='rs-prod-manufacturer-logo')
    manufacturer = man_logo.find('img')['alt']
    return manufacturer


def get_sales_rank(soup):
    ranking = soup.find(class_='ranking')
    rank = ranking.find_all('tr')[-1].find_all('td')[-1].text
    return int(rank)


def get_release(soup):
    meta_table = soup.find_all(class_='meta-table')
    date = meta_table.find_all('td')[-1].text
    return date


def scrape_guitar(page):
    thepage = url.urlopen(page)
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


def make_df(dicts):
    keys = []
    for d in dicts:
        keys += d.keys()
        keys = list(set(keys))
    data = {}
    for k in keys:
        data[k] = []
    for d in dicts:
        for k in keys:
            if k in d.keys():
                data[k].append(d[k])
            else:
                data[k].append(None)
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    landing_page = 'https://www.thomann.de/de/sonstige_westerngitarren.html?pg=%d&ls=100'
    links = []

    for i in range(1, 2):
        links += parse_list_page_for_links(landing_page % i)
    links = list(set(links))
    dicts = []
    for l in links:
        print(l)
        try:
            dicts.append(scrape_guitar(l))
        except:
            print('error')
            continue
        sleep(1)
    embed()
