from MetaGame import MetaGame
from GameTree import GameTree
import sys

mode = sys.argv[1]
root = int(sys.argv[2])

try:
    root = int(sys.argv[1])
except ValueError:
    mode = sys.argv[1]
    if mode == 'p':
        root = int(sys.argv[2])
        print(MetaGame(root))
    elif mode == 'a':
        depth = int(sys.argv[2])
        root = int(sys.argv[3])
        print(GameTree(MetaGame(root), depth+1))


