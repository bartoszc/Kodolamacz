import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.filmweb.pl/film/Narodziny+gwiazdy-2018-542576')
soup = BeautifulSoup(page.text, features='html.parser')

print(soup.find("li", itemprop="director").text)
print(soup.find("a", href="/film/Narodziny+gwiazdy-2018-542576/dates").text)
print(soup.find(text="boxoffice:").next_element.text[1:])
print(soup.find("span", itemprop="ratingValue").text)


