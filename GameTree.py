class GameTree:

    def __init__(self, game_integer):
        self.game_integer = self.__convert_to_bin(game_integer)

    def __convert_to_bin(self, game_integer):
        return int(bin(game_integer)[2:])

    def __str__(self):
        return str(self.game_integer)
