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
        elif self._meta.get_last_case().is_o():
            next_symbol = 'x'
        for child in self._children:
            if child.get_meta().winner() == next_symbol:
                return child.get_meta().get_meta_int()

        return self._count_winner(next_symbol, n)

    def _count_winner(self, symbol, n):
        """ evalue la probabilité de victoire pour chaque enfant """
        list_counters = []
        one_way = False

        for child in self._children:
            counter = 0
            meta = child.get_meta()
            for i in range(n):
                done = False
                while not done:
                    possible_moves = meta.possible_moves()
                    if len(possible_moves) == 1:
                        one_way = True                                          # si un move oblige l'adversaire a jouer a une position qui assure la victoire
                    for grand_child in possible_moves:
                        winner = grand_child.winner()
                        if winner is not None:
                            if winner == symbol:
                                if one_way:
                                    return child.get_meta().get_meta_int()
                                counter += 1
                            done = True
                            continue
                    if not done:
                        meta = random.choice(possible_moves)
            list_counters.append(counter)

        best_index = 0
        highest = list_counters[0]
        for i in range(1, len(list_counters)):
            if list_counters[i] > highest:
                highest = list_counters[i]
                best_index = i
        return self._children[best_index].get_meta().get_meta_int()

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