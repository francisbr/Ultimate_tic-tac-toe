import re

from pip._vendor.progress import counter


class MetaGame:

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
        colonne = 0;
        ligne = 0;
        str_print = ''
        for i in self.list_bin:
            if i == "00":
                str_print += " . "
            elif i == "01":
                str_print += " x "
            elif i == "10":
                str_print += " o "
            elif i == "11":
                str_print += "ERREUR"

            if colonne % 9 == 0:
                str_print += "\n"
                if ligne % 3 == 0:
                    str_print += "\n"
                ligne += 1
            if colonne % 3 == 0:
                str_print += "  "

            colonne += 1

        return str_print