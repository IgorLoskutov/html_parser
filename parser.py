from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url: str):
        self.session = requests.Session()
        self.response = self.session.get(url)
        self.soup = self._get_soup()

    def _get_soup(self):
        return BeautifulSoup(self.response.text, 'html.parser')


    def _get_containers(self, tag: str, klass: str):
        containers = self.soup.find_all(tag, klass)
        return containers


if __name__ == "__main__":

    url = 'https://play.google.com//store/apps/category/GAME'

    parser = Parser(url)
    print((parser._get_containers('a', 'r2Osbf'))[0].get('href'))






'''
class GetCategoryNames:
    def __init__(self, )


url = 'https://play.google.com//store/apps/category/GAME'
response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')


containers = soup.find_all('div', class_='action-bar-dropdown-children-container')
print(type(containedors))
all_a = containe
rs[1].find_all('a', class_ = 'submenu-container')
for _ in all_a.a:
    print(_)
'''


