class Node:

    def __init__(self, game, parent=None, children=[]):
        self._meta = game
        self._parent = parent
        self._children = children

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def get_meta(self):
        return self._meta

    def toString(self):
        return self._meta.get_meta_int()