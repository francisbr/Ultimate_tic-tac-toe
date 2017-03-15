from MetaGame import MetaGame
from GameTree import GameTree
import sys

mode = sys.argv[1]
root = int(sys.argv[2])

try:
    root = int(sys.argv[1])
except ValueError:
    mode = sys.argv[1]
    root = int(sys.argv[2])
    if mode == 'p':
        print(MetaGame(root))

# print(GameTree(MetaGame('330716890198477834926403213994701218254008155997460'), 4))

