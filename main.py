"""
main.py : Sokoban solver — interactive console menu.

Usage: python main.py
  1. Choose a level (1-5)
  2. Choose an algorithm (BFS / A* h1 / A* h2)
  → Results printed in console, then Pygame window shows the animation.
"""

import time

from gui import show_solution
from levels import LEVELS
from sokoPuzzle import SokobanPuzzle
from node import Node
from search import Search


# ----------------------------------------------------------------------
# Noufel
# ----------------------------------------------------------------------
def run(level_number, algorithm):
    board = LEVELS.get(level_number)
    if board is None:
        print(f"Level {level_number} is not available.")
        return

    initial_node = Node(SokobanPuzzle(board=board))

    print("\nInitial state:")
    print(initial_node.state)

    # --- Run chosen algorithm ---
    start = time.time()

    if algorithm == 1:
        algo_name = "BFS"
        goal_node, num_steps = Search.breadthFirst(initial_node)

    elif algorithm == 2:
        algo_name = "A* (h1)"
        goal_node, num_steps = Search.aStar(initial_node, SokobanPuzzle.h1)

    elif algorithm == 3:
        algo_name = "A* (h2)"
        goal_node, num_steps = Search.aStar(initial_node, SokobanPuzzle.h2)

    else:
        print("Invalid algorithm choice.")
        return

    elapsed = time.time() - start

    # --- Console results ---
    print(f"\n{'='*40}")
    print(f"  Algorithm  : {algo_name}")
    print(f"  Level      : {level_number}")
    print(f"{'='*40}")

    if goal_node:
        print(f"  Solution   : {goal_node.getSolution()}")
        print(f"  Path cost  : {goal_node.g}")
        print(f"  Steps expl.: {num_steps}")
        print(f"  Time       : {elapsed:.2f} s")
        print(f"{'='*40}")
        print("\nOpening Pygame window... (close it to exit)\n")
        show_solution(goal_node, algo_name=algo_name, steps=num_steps, elapsed=elapsed)
    else:
        print("  No solution found.")
        print(f"{'='*40}")


if __name__ == "__main__":
    print("╔══════════════════════════╗")
    print("║    Sokoban  Solver       ║")
    print("╚══════════════════════════╝")

    print("\nChoose a level (1-5):")
    level = int(input("  > "))

    print("\nChoose an algorithm:")
    print("  1 — BFS")
    print("  2 — A* with h1  (unplaced boxes count)")
    print("  3 — A* with h2  (h1 + Manhattan distance to nearest target)")
    algorithm = int(input("  > "))

    run(level, algorithm)
