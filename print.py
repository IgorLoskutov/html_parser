import asyncio
from concurrent.futures import ThreadPoolExecutor

from getgames import *
from getcategory import *


class Printer():
    """print games category and game names:
        /Games Starter Kit/com.kiloo.subwaysurf
        /GAME_ADVENTURE/com.webgames.ghosts"""

    def __init__(self, root_url: str):
        self.root_url = root_url
        self.cats_games = dict()

    def _get_response(self, *args):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.get_games_names(*args))
        loop.run_until_complete(future)

    async def get_games_names(self,
            cat_tag,
            cat_class,
            game_tag,
            game_class):
        """asyncronous receiving of games by category"""
        with ThreadPoolExecutor(max_workers=4) as requester:
            loop = asyncio.get_event_loop()
            task = [
                loop.run_in_executor(
                    requester,
                    self._fetch,
                    *(cat, game_tag, game_class)
                )
                for cat in self.get_cats(cat_tag, cat_class)
            ]
            for response in await asyncio.gather(*task):
                pass

    def _get_response_sync(self):
        '''just to test if asyncronous method actually
        works and gives benefits'''
        for cat in self.get_cats():
            self._fetch(cat=cat)

    def _fetch(self, cat, game_tag, game_class):
        """for each category -cat- gets list of games from the category
        page and updates dictionary storing games by category"""
        path = '/'.join([self.root_url, cat])
        games = GetGames(path)
        games.get_games(game_tag,game_class)
        self.cats_games[cat] = games.game_names
        print('fetched games: {}'.format(cat))
        return games.game_names

    def get_cats(self, cat_tag, cat_class, cat_url='GAME'):

        path = '/'.join([self.root_url, cat_url])
        cats = GetCategoryNames(path)
        cats.get_category_names(cat_tag, cat_class)
        self.cats = cats.cat_names
        print('got categories')
        return self.cats

    def print_cat_games(
        self,
        cat_tag='li',
        cat_class='KZnDLd',
        game_tag='div',
        game_class='b8cIId ReQCgd Q9MA7b'
        ):
        """default tags and classes  set accurding
            to page desing on 26/03/2019"""
        self._get_response(
            cat_tag,
            cat_class,
            game_tag,
            game_class
        )
        for c,g in self.cats_games.items():
            for game in g:
                print('/'.join([c, game]))



if __name__ == "__main__":

    url = 'https://play.google.com//store/apps/category'

    printer = Printer(url)

    printer.print_cat_games(
        cat_tag='li',
        cat_class='KZnDLd',
        game_tag='div',
        game_class='b8cIId ReQCgd Q9MA7b'
    )




