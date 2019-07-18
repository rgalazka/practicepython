"""
Wypisuje artykuły z pierwszej strony nytimes razem z linkami do nich
+ zapis do .csv
"""

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'

csv_file = open("csv_file2.csv", 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tytuł:', 'Link:'])

r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

i = 1
for wiersz in soup.find_all('article'):
    title = wiersz.h2.string
    link = 'https://www.nytimes.com' + wiersz.a.get('href')
    print(i, ') ', title, link)
    i += 1
    # link = wiersz.find('a')['href']
    # print(link)
    csv_writer.writerow([title, link])
csv_file.close()
