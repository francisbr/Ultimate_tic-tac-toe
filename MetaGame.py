from Game import Game

META_ROW = 3
META_COL = 3

class MetaGame:

    def __init__(self, meta_integer):
        self.meta_integer = self.__convert_to_bin(meta_integer)
        self.list_game = []
        self.__create_list_game(self.meta_integer)

    def __convert_to_bin(self, meta_integer):
        return bin(meta_integer)[2:]

    def __create_list_game(self, meta_integer):
        list_bin = []
        game_string = str(meta_integer)
        list_bin.append(game_string[0:7])
        for i in range(7, len(game_string), 18):
            self.list_game.append(Game(game_string[i:i+18]))

    def __str__(self):
        str_print = ''
        size = Game.GAME_ROW * Game.GAME_COL

        for k in range(META_ROW):
            str_line1 = str_line2 = str_line3 = ''
            j = 0
            for game in self.list_game[k * META_ROW:(k + 1) * META_ROW]:
                j += 1
                for i in range(len(game.get_case_list())):
                    if i % size in (0, 1, 2):
                        str_line1 += game.get_case_list()[i].toString()
                    elif i % size in (3, 4, 5):
                        str_line2 += game.get_case_list()[i].toString()
                    elif i % size in (6, 7, 8):
                        str_line3 += game.get_case_list()[i].toString()
                if j != META_COL:
                    str_line1 += " | "
                    str_line2 += " | "
                    str_line3 += " | "
            str_print += str_line1 + "\n" + str_line2 + "\n" + str_line3
            if k != META_ROW-1:
                str_print += "\n---------------------------------\n"
        return str_print
