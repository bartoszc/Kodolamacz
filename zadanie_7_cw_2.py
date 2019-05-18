import requests
from bs4 import BeautifulSoup

page = 'https://stooq.pl/q/?s='
code = input('Enther code: ')
page += code
pp = requests.get(page)
soup = BeautifulSoup(pp.text, features='html.parser')

print(f'Aktualny kurs: {soup.find(id="aq_" + code + "_c4").text}')
print(f'Procentowa zmiana: {soup.find(id="aq_" + code + "_m3").text}')
print(f'Bezwględna zmiana: {soup.find(id="aq_" + code + "_m2").text}')
print(f'Liczba transakcji: {soup.find(id="aq_" + code + "_n1").text}')


