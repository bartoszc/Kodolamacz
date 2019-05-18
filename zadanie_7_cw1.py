import requests
from bs4 import BeautifulSoup

page = requests.get('https://sportowefakty.wp.pl/zuzel')
soup = BeautifulSoup(page.text, features='html.parser')

for link in soup.find_all('a', href=True):
    print(link)
