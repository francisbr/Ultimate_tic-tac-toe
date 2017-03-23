import random

class Node:

    def __init__(self, meta_game, depth, parent=None):
        self._meta = meta_game
        self._parent = parent
        self._depth = depth
        self._children = []

    def best_move(self, n):
        """
        Détermine lequel des enfants donne le plus de chances de gagner la partie
        :param n: nombre de tests par enfant
        :return: l'enfant ayant la plus grande probabilite de l'emporter
        """
        if self._meta.get_last_case().is_x():
            next_symbol = 'o'
        else:
            next_symbol = 'x'
        for child in self._children:
            if child.get_meta().winner() == next_symbol:
                return child.get_meta()

        return self._count_winner(next_symbol, n)

    def _count_winner(self, symbol, n):
        """ evalue la probabilité de victoire pour chaque enfant """
        list_counters = []

        for child in self._children:
            counter = 0
            for i in range(n):
                meta = child.get_meta()
                done = False
                length_game = 0
                while not done:
                    possible_moves = meta.possible_moves()
                    for grand_child in possible_moves:
                        winner = grand_child.winner()
                        length_game += 1
                        if length_game > 10:                # le programme ne regarde pas plus de 10 coups à l'avance
                            done = True
                            break
                        if winner is not None:
                            if winner == symbol:
                                counter += 1
                            done = True
                            break
                    if not done:
                        meta = random.choice(possible_moves)
            if counter == 1000:
                return child.get_meta()
            list_counters.append(counter)
        highest = list_counters[0]
        best_index = 0
        for i in range(1, len(list_counters)):
            if list_counters[i] > highest:
                highest = list_counters[i]
                best_index = i
        return self._children[best_index].get_meta()

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def nb_children(self):
        return int(len(self._children))

    def get_meta(self):
        return self._meta

    def get_depth(self):
        return self._depth

    def toString(self):
        return self._meta.get_meta_int()