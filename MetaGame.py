from Game import Game

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
            self.list_game.append(Game(game_string[i:i+18], (i-7)/18))

    def __str__(self):
        colonne = 0;
        ligne = 0;
        str_print = ''

        for i in self.list_game:
            str_print += i.toString()

        # for i in self.list_bin:
        #     if i == "00":
        #         str_print += " . "
        #     elif i == "01":
        #         str_print += " x "
        #     elif i == "10":
        #         str_print += " o "
        #     elif i == "11":
        #         str_print += "ERREUR"
        #
        #     if colonne % 9 == 0:
        #         str_print += "\n"
        #         if ligne % 3 == 0:
        #             str_print += "\n"
        #         ligne += 1
        #     if colonne % 3 == 0:
        #         str_print += "  "
        #
        #     colonne += 1
        return str_print