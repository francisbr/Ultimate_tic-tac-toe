import random

class Node:

    def __init__(self, meta_game, depth, parent=None):
        self._meta = meta_game
        self._parent = parent
        self._depth = depth
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def sample(self, n):
        list_counters_x = []
        list_counters_o = []
        if self._meta.get_last_case().is_x():
            next_symbol = 'o'
        elif self._meta.get_last_case().is_o():
            next_symbol = 'x'
        for child in self._children:
            if child.get_meta().winner() == next_symbol:
                return child.get_meta().get_meta_int()
        for child in self._children:
            counter_x = 0
            counter_o = 0
            meta = child.get_meta()
            for i in range(n):
                done = False
                while not done:
                    possible_moves = meta.possible_moves()
                    for grand_child in possible_moves:
                        winner = grand_child.winner()
                        if winner is not None:
                            if winner == 'x':
                                counter_x += 1
                            elif winner == 'o':
                                counter_o += 1
                            done = True
                            continue
                    if not done:
                        meta = random.choice(possible_moves)
            list_counters_x.append(counter_x)
            list_counters_o.append(counter_o)

        best_index = 0
        if next_symbol == 'x':
            highest = list_counters_x[0]
            for i in range(1, len(list_counters_x)):
                if list_counters_x[i] > highest:
                    highest = list_counters_x[i]
                    best_index = i
        else:
            highest = list_counters_o[0]
            for i in range(1, len(list_counters_o)):
                if list_counters_o[i] > highest:
                    highest = list_counters_o[i]
                    best_index = i

        return self._children[best_index].get_meta().get_meta_int()

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