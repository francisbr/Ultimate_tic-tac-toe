from Game import Game

META_ROW = 3
META_COL = 3

class MetaGame:

    def __init__(self, meta_integer):
        self._meta_bin = self.__convert_to_bin(meta_integer)
        self._last_move = int(self._meta_bin[0:7], 2)
        self._list_game = []
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
        for i in range(7, len(self._meta_bin), bits_per_game):
            if (i - 7)//2 <= self._last_move < ((i - 7) + bits_per_game)//2:   # si le dernier mouvement se trouve dans cette partie
                self._list_game.append(Game(self._meta_bin[i:i + bits_per_game], (i - 7)/bits_per_game, self._last_move))
            else:
                self._list_game.append(Game(self._meta_bin[i:i + bits_per_game], (i - 7)/bits_per_game))

    def get_last_move(self):
        return self._last_move

    def get_game(self, position):
        return self._list_game[position]

    def get_meta_bin(self):
        return self._meta_bin

    def get_meta_int(self):
        return str(int(self._meta_bin, 2))

    def empty_cases(self):
        for game in self._list_game:
            if not game.is_won():
                for case in game.empty_cases():
                    yield case

    def is_won(self):
        games_won = [self._list_game[0].is_won(), self._list_game[1].is_won(), self._list_game[2].is_won(),
                     self._list_game[3].is_won(), self._list_game[4].is_won(), self._list_game[5].is_won(),
                     self._list_game[6].is_won(), self._list_game[7].is_won(), self._list_game[8].is_won()]

        if  (games_won[0] == games_won[4] == games_won[8]) or \
            (games_won[1] == games_won[4] == games_won[7]) or \
            (games_won[3] == games_won[4] == games_won[5]) or \
            (games_won[4] == games_won[6] == games_won[2]):
                if games_won[4] is not None:
                    return games_won[4]
        if  (games_won[2] == games_won[5] == games_won[8]) or \
            (games_won[6] == games_won[7] == games_won[8]):
                if games_won[8] is not None:
                    return games_won[8]
        if  (games_won[0] == games_won[1] == games_won[2]) or \
            (games_won[0] == games_won[3] == games_won[6]):
                if games_won[0] is not None:
                    return games_won[0]
        return None

    def __str__(self):
        str_print = ''
        game_size = Game.GAME_ROW * Game.GAME_COL

        for k in range(META_ROW):
            str_line1 = str_line2 = str_line3 = ''
            j = 0
            for game in self._list_game[k * META_COL:(k + 1) * META_COL]:
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
