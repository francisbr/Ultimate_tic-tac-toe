from Case import Case


class Game:

    GAME_ROW = 3
    GAME_COL = 3

    def __init__(self, game_bin, position, last_move=-1):
        self._size = self.GAME_COL * self.GAME_ROW
        self._position = position
        self._last_move = last_move
        self._list_case = []
        self.__create_list(game_bin)

    def __create_list(self, game_bin):
        for i in range(0, len(game_bin), 2):
            if self._last_move % (self._size * 2) == i//2:
                self._list_case.append(Case(game_bin[i:i + 2], (i//2) + (self._position * 9), True))
            else:
                self._list_case.append(Case(game_bin[i:i + 2], (i//2) + (self._position * 9)))

    def get_case_list(self):
        return self._list_case

    def get_case(self, position):
        return self._list_case[position]

    def empty_cases(self):
        list_empty = []
        for case in self._list_case:
            if case.is_empty():
                list_empty.append(case)
        return list_empty

    def get_position(self):
        return self._position
