from MetaGame import MetaGame
from GameTree import GameTree
import sys
import timing

try:
    root = int(sys.argv[1])
    tree = GameTree(MetaGame(root), 2)
    print(tree.root().best_move(1000).get_meta_int())
except ValueError:
    mode = sys.argv[1]
    if mode == 'p':
        root = int(sys.argv[2])
        print(MetaGame(root))
    elif mode == 'a':
        depth = int(sys.argv[2])
        root = int(sys.argv[3])
        print(GameTree(MetaGame(root), depth+1))

