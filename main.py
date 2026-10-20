"""
main.py : lance le BFS sur un des 5 niveaux et affiche le résultat.
Usage :  python main.py        (niveau 1 par défaut)
         python main.py 3      (niveau 3)
"""


import time

from levels import LEVELS
from sokoPuzzle import SokobanPuzzle
from node import Node
from search import Search


# ----------------------------------------------------------------------
# MEMBRE 3
# ----------------------------------------------------------------------
def run(level_number):
    board = LEVELS[level_number]
    if board is None:
        print(f"Le niveau {level_number} n'est pas encore encodé dans levels.py")
        return

    initial_node = Node(SokobanPuzzle(board=board))

    print("Etat initial :")
    print(initial_node.state)

    start = time.time()
    goal_node, num_steps = Search.breadthFirst(initial_node)
    elapsed = time.time() - start

    if goal_node:
        print(f"Optimal Solution found after {num_steps} steps")
        print("Solution :", goal_node.getSolution())
        print("Cout du chemin :", goal_node.g)
        print(f"Temps : {elapsed:.2f} s")
        # TODO (optionnel) : afficher goal_node.getPath() étape par étape
    else:
        print("Optimal solution not found ")


if __name__ == "__main__":
    level = int(input("veulliez entrer le niveaux desirer :\n"))
    run(level)
