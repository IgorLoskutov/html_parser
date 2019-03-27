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

    def _get_response(self):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.get_games_names())
        loop.run_until_complete(future)

    async def get_games_names(self):
        self.get_cats()
        with ThreadPoolExecutor(max_workers=5) as requester:
            loop = asyncio.get_event_loop()
            task = [
                loop.run_in_executor(
                    requester,
                    self.fetch,
                    (cat)
                )
                for cat in self.cats
            ]
            for response in await asyncio.gather(*task):
                pass

    def _get_response_sync(self):
        for cat in self.get_cats('GAME','li', 'KZnDLd'):
            self.fetch(cat, 'div', 'b8cIId ReQCgd Q9MA7b')

    def fetch(self, cat, game_tag='div', game_class='b8cIId ReQCgd Q9MA7b'):
        path = '/'.join([self.root_url, cat])
        #print(path)
        games = GetGames(path)
        games.get_games(game_tag,game_class)
        self.cats_games[cat] = games.game_names
        print('fetched games: {}'.format(cat))
        return games.game_names

    def get_cats(self, cat_url='GAME', cat_tag='li', cat_class='KZnDLd'):
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
        self._get_response()
        for c,g in printer.cats_games.items():
            for game in g:
                print('/'.join([c, game]))



if __name__ == "__main__":

    url = 'https://play.google.com//store/apps/category'

    printer = Printer(url)

    cat_tag='li'
                      cat_class='KZnDLd'
                    game_tag='div'
                    game_class='b8cIId ReQCgd Q9MA7b'

    printer.print_cat_games()




