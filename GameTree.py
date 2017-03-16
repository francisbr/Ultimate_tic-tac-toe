from Node import Node
from MetaGame import MetaGame
from ArrayQueue import ArrayQueue


class GameTree:
    def __init__(self, root, depth):
        last_move = root.get_last_move()
        self._root = Node(root, 0)
        self._depth = depth
        self._create_children(last_move, self._root, 1)

    def _create_children(self, last_move, current, x):
        if x == self._depth or current.get_meta().is_won() is not None:
            return
        else:
            current_meta_bin = current.get_meta().get_meta_bin()
            for i in range(0, 80, 9):
                if i <= last_move < i + 9:
                    last_case = current.get_meta().get_game(i // 9).get_case(last_move % 9)
            next_game = current.get_meta().get_game(last_move % 9)
            if next_game.is_won() is not None:
                next_game = current.get_meta()
            for case in next_game.empty_cases():
                if last_case.is_x():
                    new_meta_bin = case.get_bin_position() + \
                                   current_meta_bin[7:7 + (2 * case.get_position())] + \
                                   '10' + \
                                   current_meta_bin[9 + (2 * case.get_position()):170]
                else:
                    new_meta_bin = case.get_bin_position() + \
                                   current_meta_bin[7:7 + (2 * case.get_position())] + \
                                   '01' + \
                                   current_meta_bin[9 + (2 * case.get_position()):170]
                new_child = Node(MetaGame(str(int(new_meta_bin, 2))), x, current)
                current.add_child(new_child)
                self._create_children(case.get_position(), new_child, x + 1)

    def __str__(self):
        str_return = ''
        q_uttt = ArrayQueue()
        q_uttt.enqueue(self._root)
        last_depth = 0
        while not q_uttt.is_empty():
            child = q_uttt.dequeue()
            if last_depth != child.get_depth():
                str_return += "\n\n"
            str_return += child.get_meta().get_meta_int() + ' '
            last_depth = child.get_depth()
            for grand_child in child.get_children():
                q_uttt.enqueue(grand_child)
        return str_return
