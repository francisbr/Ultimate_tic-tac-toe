import re

class GameTree:

    def __init__(self, game_integer):
        self.game_integer = self.__convert_to_bin(game_integer)
        self.list_bin = []
        self.__create_list(self.game_integer)

    def __convert_to_bin(self, game_integer):
        return int(bin(game_integer)[2:])

    def __create_list(self, game_integer):
        game_string = str(game_integer)
        self.list_bin.append(game_string[0:7])
        for i in range(0, len(game_string)):
            self.list_bin.append(game_string[(i*2)+7:(i*2)+9])

    def __str__(self):
        str_print = ''
        for i in self.list_bin:
            str_print += (i + "\n")
        return str_print