class Node:

    def __init__(self, meta_game, parent=None):
        self._meta = meta_game
        self._parent = parent
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def nb_children(self):
        return int(len(self._children))

    def get_meta(self):
        return self._meta

    def toString(self):
        return self._meta.get_meta_int()