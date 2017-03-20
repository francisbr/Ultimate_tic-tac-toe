from Game import Game

META_ROW = 3
META_COL = 3

class MetaGame:

    def __init__(self, meta_integer):
        self._meta_bin = self.__convert_to_bin(meta_integer)
        self._last_move = int(self._meta_bin[0:7], 2)
        self._list_game = []
        self.__create_list_game()
        for i in range(0, 80, 9):
            if i <= self._last_move < i + 9:
                self._last_case = self.get_game(i // 9).get_case(self._last_move % 9)

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
        """ place des elements dans la meta-game"""
        bits_per_game = Game.GAME_ROW * Game.GAME_COL * 2
        for i in range(7, len(self._meta_bin), bits_per_game):
            if (i - 7)//2 <= self._last_move < ((i - 7) + bits_per_game)//2:   # si le dernier mouvement se trouve dans cette partie
                self._list_game.append(Game(self._meta_bin[i:i + bits_per_game], (i - 7)/bits_per_game, self._last_move))
            else:
                self._list_game.append(Game(self._meta_bin[i:i + bits_per_game], (i - 7)/bits_per_game))

    def possible_moves(self):
        """ retourne les mouvements qu'il est possible d'effectuer a partir de la configuration actuelle """
        list_moves = []
        next_game = self.get_game(self._last_move % 9)
        if next_game.winner() is not None:              # si la sous-partie est gagnée ou est pleine
            for game in self._list_game:
                game_winner = game.winner()
                if game_winner is None and game_winner != 'n':
                    for case in game.empty_cases():
                        next_int = self.get_int(case.get_bin_position())
                        list_moves.append(MetaGame(next_int))
        else:
            for case in next_game.empty_cases():
                next_int = self.get_int(case.get_bin_position())
                list_moves.append(MetaGame(next_int))

        return list_moves

    def get_int(self, move):
        """ retounre l'entier de la configuration suivant le coup < move >"""
        if self._last_case.is_x():
            return int(move + self._meta_bin[7:7 + (2 * int(move, 2))] + '10' + self._meta_bin[9 + (2 * int(move, 2)):170], 2)
        elif self._last_case.is_o():
            return int(move + self._meta_bin[7:7 + (2 * int(move, 2))] + '01' + self._meta_bin[9 + (2 * int(move, 2)):170], 2)

    def get_last_move(self):
        return self._last_move

    def get_last_case(self):
        return self._last_case

    def get_game(self, position):
        return self._list_game[position]

    def get_meta_bin(self):
        return self._meta_bin

    def get_meta_int(self):
        return str(int(self._meta_bin, 2))

    def winner(self):
        """ retourne le gagnat de la meta-game ou indique qu'elle est nulle """
        games_winner = [self._list_game[0].winner(), self._list_game[1].winner(), self._list_game[2].winner(),
                        self._list_game[3].winner(), self._list_game[4].winner(), self._list_game[5].winner(),
                        self._list_game[6].winner(), self._list_game[7].winner(), self._list_game[8].winner()]

        if  (games_winner[0] == games_winner[4] == games_winner[8]) or \
            (games_winner[1] == games_winner[4] == games_winner[7]) or \
            (games_winner[3] == games_winner[4] == games_winner[5]) or \
            (games_winner[6] == games_winner[4] == games_winner[2]):
                if games_winner[4] is not None and games_winner[4] != 'n':
                    return games_winner[4]
        elif (games_winner[2] == games_winner[5] == games_winner[8]) or \
             (games_winner[6] == games_winner[7] == games_winner[8]):
                if games_winner[8] is not None and games_winner[8] != 'n':
                    return games_winner[8]
        elif (games_winner[0] == games_winner[1] == games_winner[2]) or \
             (games_winner[0] == games_winner[3] == games_winner[6]):
                if games_winner[0] is not None and games_winner[0] != 'n':
                    return games_winner[0]
        elif (games_winner[0] is not None and games_winner[1] is not None and games_winner[2] is not None and
              games_winner[3] is not None and games_winner[4] is not None and games_winner[5] is not None and
              games_winner[6] is not None and games_winner[7] is not None and games_winner[8] is not None):
            return 'n'
        else:
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
