from Node import Node
from MetaGame import MetaGame

class GameTree:
    """Abstract base representing a tree structure."""

# ------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')
        def eq(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def ne(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of     eq

    def __init__(self, root, depth):
        last_move = root.get_last_move()
        self._root = Node(root)
        self._depth = depth
        self._create_children(last_move, self._root, self._depth)

    def _create_children(self, last_move, current, n):
        current_meta_bin = current.get_meta().get_meta_bin()
        for i in range(0, 80, 9):
            if i <= last_move < i+9:
                last_case = self._root.get_meta().get_game(i//9).get_case(last_move % 9)
        next_game = self._root.get_meta().get_game(last_move % 9)
        for case in next_game.empty_cases():
            if last_case.is_x():
                new_meta_bin = case.get_bin_position() + \
                               current_meta_bin[7:7+(2 * case.get_position())] + \
                               '10' + \
                               current_meta_bin[9+(2 * case.get_position()):170]
            else:
                new_meta_bin = case.get_bin_position() + \
                               current_meta_bin[7:7 + (2 * case.get_position())] + \
                               '01' + \
                               current_meta_bin[9 + (2 * case.get_position()):170]
            current.add_child(Node(MetaGame(str(int(new_meta_bin, 2))), current))

    def __str__(self):
        str_return = self._root.toString() + '\n'
        for child in self._root.get_children():
            str_return += ' ' + child.toString()
        return str_return