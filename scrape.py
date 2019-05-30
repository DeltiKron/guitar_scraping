import urllib.request as url
from time import sleep

import bs4
from IPython import embed


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


def scrape_guitar(page):
    """Scrape attributes from a guitar info page
    :param page: URL to info page
    :return: dictionary of attributes parsed from page
    """
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

    def clean_key(instring):
        '''reformatting for locale reasons, minor'''
        outstring = instring
        outstring = outstring.replace(' ', '_')
        outstring = outstring.replace('.', '_')
        outstring = outstring.replace('__', '_')
        return outstring

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
