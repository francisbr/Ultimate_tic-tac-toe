from Case import Case


class Game:

    GAME_ROW = 3
    GAME_COL = 3

    def __init__(self, game_bin, position, last_move=-1):
        self._size = self.GAME_COL * self.GAME_ROW
        self._position = int(position)
        self._last_move = last_move
        self._list_case = []
        self.__create_list(game_bin)

    def __create_list(self, game_bin):
        for i in range(0, len(game_bin), 2):
            if self._last_move >= 0 and self._last_move % self._size == i//2:
                self._list_case.append(Case(game_bin[i:i + 2], (i//2) + (self._position * 9), True))
            else:
                self._list_case.append(Case(game_bin[i:i + 2], (i//2) + (self._position * 9)))

    def get_case_list(self):
        return self._list_case

    def get_case(self, position):
        return self._list_case[position]

    def empty_cases(self):
        for case in self._list_case:
            if case.is_empty():
                yield case

    def is_won(self):
        if  self._list_case[0] == self._list_case[4] == self._list_case[8] or \
            self._list_case[1] == self._list_case[4] == self._list_case[7] or \
            self._list_case[3] == self._list_case[4] == self._list_case[5] or \
            self._list_case[4] == self._list_case[6] == self._list_case[2]:
                if self._list_case[4].is_x():
                    return 'x'
                elif self._list_case[4].is_o():
                    return 'o'
        if  self._list_case[0] == self._list_case[1] == self._list_case[2] or \
            self._list_case[0] == self._list_case[3] == self._list_case[6]:
                if self._list_case[0].is_x():
                    return 'x'
                elif self._list_case[0].is_o():
                    return 'o'
        if  self._list_case[2] == self._list_case[5] == self._list_case[8] or \
            self._list_case[6] == self._list_case[7] == self._list_case[8]:
                if self._list_case[8].is_x():
                    return 'x'
                elif self._list_case[8].is_o():
                    return 'o'
        return None

    def get_position(self):
        return self._position
