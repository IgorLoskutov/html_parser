from getcategory import*


class GetGames:

    def __init__(self, url:str):
        self.parser = (Parser(url))

    def get_games(self, tag, klass):
        self.game_names = set()
        game_urls = self.parser._get_containers(tag, klass)
        for url in game_urls:
            game = url.a.get('href').split('=')[-1]
            self.game_names.add(game)
        return self.game_names



if __name__ == "__main__":

    url = 'https://play.google.com//store/apps/category/GAME'

    cat = GetCategoryNames(url)
    tag = 'div'
    klass = 'b8cIId ReQCgd Q9MA7b'

    categories = cat.get_category_names(tag, klass)

    print(categories)

    games = GetGames('https://play.google.com//store/apps/category/GAME_CASINO')
    games.get_games('div', 'b8cIId ReQCgd Q9MA7b')
    print(len(games.game_names))