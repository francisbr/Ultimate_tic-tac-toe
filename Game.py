from Case import Case

class Game:

    def __init__(self, game_bin, position):
        self.game_list = self.__create_list(game_bin)
        self.position = position

    def __create_list(self, game_bin):
        list = []
        for i in range(0, len(game_bin), 2):
            list.append(Case(game_bin[i:i+2], self.position + i/2))
        return list

    def toString(self):
        string_game = ''
        for i in self.game_list:
            string_game += i.toString()
        return string_game