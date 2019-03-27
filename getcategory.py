from parser import *


class GetCategoryNames(object):
    """getting category by url"""

    def __init__(self, url: str):
        self.url = url
        self.parser = Parser(url)


    def get_category_names(self, tag, klass):
        '''arrange set of category names from uls listed on the page'''
        self.cat_names = set()
        category_urls = self.parser._get_containers(tag, klass)
        for url in category_urls:
            if 'category/GAME' in url.a.get('href'):
                self.cat_names.add(url.a.get('href').split('/')[-1])
        return self.cat_names



if __name__ == "__main__":

    url = 'https://play.google.com//store/apps/category/GAME'

    cat = GetCategoryNames(url)

    tag = 'li'
    klass = 'KZnDLd'

    print(cat.get_category_names(tag, klass))

