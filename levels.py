"""
levels.py : les 5 exemples de test du PDF (Figure 4).

Légende : 'O' mur | ' ' vide | 'S' cible | 'B' caisse | 'R' robot
          '*' caisse sur cible | '.' robot sur cible

Chaque ligne doit avoir EXACTEMENT la même longueur (grille rectangulaire :
complétez avec des 'O' à l'extérieur du labyrinthe si besoin).

Coût optimal attendu (valeurs du programme de la prof) :
    board1 -> 4 | board2 -> 29 | board3 -> 33 | board4 -> 30 | board5 -> 25
"""

# Exemple 1 : repris de la capture du code de la prof (coût attendu : 4)
board1 = [
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'S', ' ', 'B', ' ', 'O'],
    ['O', ' ', 'O', 'R', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
]

# ----------------------------------------------------------------------
# MEMBRE 1 : à encoder en regardant la Figure 4 du PDF, case par case.
# Astuce : compter lignes/colonnes sur l'image, puis vérifier avec
# print(SokobanPuzzle(boardX)) que l'affichage ressemble à l'image.
# ----------------------------------------------------------------------

# Exemple 2 (coût attendu : 29)
board2 = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['O', ' ', ' ', 'O', 'O', 'O', ' ', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', 'O', '.', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
    ['O', ' ', ' ', 'B', ' ', ' ', 'O', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
]

# Exemple 3 (coût attendu : 33)
board3 = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', ' ', ' ', ' ', 'O', ' ', ' ', 'O'],
    ['O', ' ', ' ', 'B', 'R', ' ', ' ', 'O'],
    ['O', ' ', ' ', ' ', 'O', 'B', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
    ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
]

# Exemple 4 (coût attendu : 30)
board4 = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
    ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
    ['O', 'O', ' ', '*', ' ', ' ', 'O'],
    ['O', 'O', 'B', 'O', 'B', ' ', 'O'],
    ['O', ' ', 'S', 'R', 'S', ' ', 'O'],
    ['O', ' ', ' ', ' ', ' ', 'O', 'O'],
    ['O', 'O', 'O', ' ', ' ', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O']
]

# Exemple 5 (coût attendu : 25)
board5 = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'S', 'O', ' ', ' ', 'O', 'O'],
    ['O', ' ', ' ', ' ', ' ', 'B', ' ', 'O', 'O'],
    ['O', ' ', 'B', ' ', 'R', ' ', ' ', 'S', 'O'],
    ['O', 'O', 'O', ' ', 'O', ' ', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'B', 'O', ' ', 'O', 'O', 'O'],
    ['O', 'O', 'O', ' ', ' ', 'S', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
]


LEVELS = {
    1: board1,
    2: board2,
    3: board3,
    4: board4,
    5: board5,
}
