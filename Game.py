from Case import Case


class Game:

    GAME_ROW = 3
    GAME_COL = 3

    def __init__(self, game_bin):
        self.case_list = self.__create_list(game_bin)

    def __create_list(self, game_bin):
        list = []
        for i in range(0, len(game_bin), 2):
            list.append(Case(game_bin[i:i+2]))
        return list

    def get_case_list(self):
        return self.case_list