"""
Wypisuje artykuły z pierwszej strony nytimes razem z linkami do nich
+ zapis do .csv
"""

import requests
import bs4
from bs4 import BeautifulSoup

# import csv

url = 'https://www.wp.pl'

# csv_file = open("csv_file2.csv", 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Tytuł:', 'Link:'])

r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

find = soup.find_all('a')
Dic = {}
i = 1
for wiersz in find:
    if len(wiersz.text) > 15:
        print(i, ') ', wiersz.text, ' -> ', wiersz.get('href'))
        Dic[i] = wiersz.get('href')
        i += 1
# csv_writer.writerow([title, link])
# csv_file.close()
# url2 = 'https://wiadomosci.wp.pl/tragiczny-wypadek-na-a4-w-malopolsce-jedna-osoba-zginela-sa-ranni-6401291426387585a'
for k in Dic:
    # print(Dic[k])
    np = str(Dic[k])
    if np[0:4] == 'http':
        print(np)
        r2_html = requests.get(Dic[k]).text
        soup2 = BeautifulSoup(r2_html, "html.parser")
        # if soup2.find('div', class_='article--lead') is True:
        if soup2.find('div', class_='article--lead') is not None:
            #print('jest intro !!!!!!!!!!!!!!!!')
            print('(div) ',soup2.find('div', class_='article--lead').text)
        elif soup2.find('article', class_='article desktop video') is not None:
            print('art video !!!!!!!!!!!!!!!!')

            #print('(article.string) ', soup2.find('article').h5.string)
        elif soup2.find('article', class_='article') is not None:
            print('(article.string) ',soup2.find('article').text)
        else:
            print('brak intro')
    # else:
    #     print(None)
    #         # r2_html = requests.get(Dic[k]).text
    # soup2 = BeautifulSoup(r2_html, "html.parser")
    # print(soup2.find('div', class_='article--lead').text)

    # TODO: upewnic się ze początek adresu ma http:// i że po wejściu w artykól jest tam znacznik <dev article--lead>zajawki
