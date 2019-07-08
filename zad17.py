import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
title=[]
soup = BeautifulSoup(r_html, "html.parser")
#title = soup.find('h2')
for i in soup:
    title.append(soup.find('h2'))
#    title.append(soup.title.string)

print(title)
#print(r_html[100000:200000])