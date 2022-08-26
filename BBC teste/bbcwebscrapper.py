import requests
from bs4 import BeautifulSoup
import os


def BBCWebScrapper(url):
    # https://www.bbc.com/news/world
  #  url = input("insira o URL: ")
  #url = url_entry.get()
    url_print = 'URL -' + url + '\n' + '\n'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.105 Safari/537.36 Vivaldi/5.4.2753.40" }

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    noticias = soup. find_all('div', class_='gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--flex gs-u-mt@xs gs-u-mt0@xs gs-u-mt@m gel-1/2@xs gel-1/1@s')

    # noticia = noticias[0]
    if os.path.exists("noticias_lista.txt"):
        os.remove("noticias_lista.txt")

    with open  ('noticias_lista.txt', 'a', newline='', encoding = 'UTF-8') as f:
        f.write(url_print)
        for noticia in noticias : 
            title = noticia.find('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor').get_text()
            text = noticia.find('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m').get_text()
            value = title + ' - ' + text + '\n'+ '\n'        
            f.write(value) 
