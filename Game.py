from Case import Case


class Game:

    GAME_ROW = 3
    GAME_COL = 3

    def __init__(self, game_bin, last_move=None):
        self.size = self.GAME_COL * self.GAME_ROW
        self.last_move = last_move
        self.case_list = self.__create_list(game_bin)

    def __create_list(self, game_bin):
        list = []
        if self.last_move is None:
            for i in range(0, len(game_bin), 2):
                list.append(Case(game_bin[i:i+2]))
        else:
            for i in range(0, len(game_bin), 2):
                if self.last_move % (self.size * 2) == i//2:
                    list.append(Case(game_bin[i:i + 2], True))
                else:
                    list.append(Case(game_bin[i:i + 2]))
        return list

    def get_case_list(self):
        return self.case_list