from Game import Game

META_ROW = 3
META_COL = 3

class MetaGame:

    def __init__(self, meta_integer):
        self.meta_bin = self.__convert_to_bin(meta_integer)
        print(self.meta_bin)
        self.list_game = []
        self.__create_list_game()

    def __convert_to_bin(self, str_integer):
        """
        convertir l'entier de depart en binaire
        :param str_integer: entier du jeu
        :return: entier du jeu en nombre binaire de 169 bits sous forme de String
        """
        str_bin = str(bin(int(str_integer))[2:])
        while len(str_bin) < 169:
            str_bin = "0" + str_bin
        return str_bin

    def __create_list_game(self):
        bits_per_game = Game.GAME_ROW * Game.GAME_COL * 2
        last_move = int(self.meta_bin[0:7], 2)
        for i in range(7, len(self.meta_bin), bits_per_game):
            if (i - 7)//2 <= last_move < ((i - 7) + bits_per_game)//2:
                self.list_game.append(Game(self.meta_bin[i:i + bits_per_game], last_move))
            else:
                self.list_game.append(Game(self.meta_bin[i:i + bits_per_game]))

    def __str__(self):
        str_print = ''
        game_size = Game.GAME_ROW * Game.GAME_COL

        for k in range(META_ROW):
            str_line1 = str_line2 = str_line3 = ''
            j = 0
            for game in self.list_game[k * META_COL:(k + 1) * META_COL]:
                j += 1
                for i in range(len(game.get_case_list())):
                    if i % game_size in (0, 1, 2):
                        str_line1 += game.get_case_list()[i].toString()
                    elif i % game_size in (3, 4, 5):
                        str_line2 += game.get_case_list()[i].toString()
                    elif i % game_size in (6, 7, 8):
                        str_line3 += game.get_case_list()[i].toString()
                if j != META_COL:
                    str_line1 += " | "
                    str_line2 += " | "
                    str_line3 += " | "
            str_print += str_line1 + "\n" + str_line2 + "\n" + str_line3
            if k != META_ROW-1:
                str_print += "\n-----------------------------\n"
        return str_print
