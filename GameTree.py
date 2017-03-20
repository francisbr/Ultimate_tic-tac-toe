from Node import Node
from MetaGame import MetaGame
from ArrayQueue import ArrayQueue


class GameTree:
    def __init__(self, root, depth):
        self._root = Node(root, 0)
        self._depth = depth
        self._create_children(self._root, 1)

    def _create_children(self, current, x):
        """ cree un arbre a partir d'une racine """
        if x == self._depth or current.get_meta().winner() is not None:
            return
        else:
            for meta in current.get_meta().possible_moves():
                new_child = Node(meta, x, current)
                current.add_child(new_child)
                self._create_children(new_child, x + 1)

    def root(self):
        return self._root

    def __str__(self):
        str_return = ''
        q_uttt = ArrayQueue()
        q_uttt.enqueue(self._root)
        last_depth = 0
        while not q_uttt.is_empty():
            child = q_uttt.dequeue()
            if last_depth != child.get_depth():
                str_return += "\n"
            str_return += child.get_meta().get_meta_int() + ' '
            last_depth = child.get_depth()
            for grand_child in child.get_children():
                q_uttt.enqueue(grand_child)
        return str_return
