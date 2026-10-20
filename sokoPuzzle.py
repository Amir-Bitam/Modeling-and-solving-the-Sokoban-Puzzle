"""
sokoPuzzle.py : modélisation de l'état du jeu Sokoban.

Légende du board d'entrée (liste de listes de caractères) :
    'O' => mur
    ' ' => case vide
    'S' => cible (storage)
    'B' => caisse (box)
    'R' => robot
    '*' => caisse sur une cible
    '.' => robot sur une cible

Le board est séparé en deux grilles :
    - wall_space_obstacle : éléments STATIQUES  -> 'O', 'S', ' '
    - robot_block         : éléments DYNAMIQUES -> 'R', 'B', ' '
Ainsi, un robot ou une caisse qui passe sur une cible n'efface jamais la cible.
"""

from copy import deepcopy


class SokobanPuzzle:

    # Action -> déplacement (ligne, colonne). CONTRAT : ne pas changer les clés.
    DIRECTIONS = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    # ------------------------------------------------------------------
    # MEMBRE 1
    # ------------------------------------------------------------------
    def __init__(self, board):
        # On separe la grille fixe et la grille mobile.
        self.height = len(board)
        self.width = len(board[0])
        self.wall_space_obstacle = []
        self.robot_block = []
        self.robot_position = (0, 0)

        for i in range(self.height):
            ligne_statique = []
            ligne_mobile = []
            for j in range(self.width):
                c = board[i][j]
                if c == 'R':
                    ligne_statique.append(' ')
                    ligne_mobile.append('R')
                    self.robot_position = (i, j)
                elif c == '.':
                    ligne_statique.append('S')
                    ligne_mobile.append('R')
                    self.robot_position = (i, j)
                elif c == 'B':
                    ligne_statique.append(' ')
                    ligne_mobile.append('B')
                elif c == '*':
                    ligne_statique.append('S')
                    ligne_mobile.append('B')
                elif c == 'S':
                    ligne_statique.append('S')
                    ligne_mobile.append(' ')
                elif c == 'O':
                    ligne_statique.append('O')
                    ligne_mobile.append(' ')
                else:
                    ligne_statique.append(' ')
                    ligne_mobile.append(' ')
            self.wall_space_obstacle.append(ligne_statique)
            self.robot_block.append(ligne_mobile)

        self.moves = ["U", "D", "L", "R"]

    def isGoal(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.wall_space_obstacle[i][j] == 'S':
                    if self.robot_block[i][j] != 'B':
                        return False
        return True

    def __eq__(self, other):
        return self.robot_block == other.robot_block

    def __hash__(self):
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s += self.robot_block[i][j]
            s += "|"
        return hash(s)

    def __str__(self):
        texte = ""
        for i in range(self.height):
            ligne = ""
            for j in range(self.width):
                mobile = self.robot_block[i][j]
                statique = self.wall_space_obstacle[i][j]
                if mobile == 'R':
                    if statique == 'S':
                        ligne += '.'
                    else:
                        ligne += 'R'
                elif mobile == 'B':
                    if statique == 'S':
                        ligne += '*'
                    else:
                        ligne += 'B'
                else:
                    ligne += statique
            texte += ligne
            if i < self.height - 1:
                texte += "\n"
        return texte

    # ------------------------------------------------------------------
    # MEMBRE 2
    # ------------------------------------------------------------------
    def successorFunction(self):
        """
        Retourne la liste des paires (action, successeur) pour tous les
        mouvements valides depuis cet état.
            -> [("U", SokobanPuzzle), ("R", SokobanPuzzle), ...]

        TODO : pour chaque action dans self.moves :
            (di, dj) = DIRECTIONS[action]
            (ri, rj) = self.robot_position
            (ni, nj) = (ri + di, rj + dj)          # case d'arrivée du robot

            1. Si wall_space_obstacle[ni][nj] == 'O'  -> mouvement invalide.

            2. Si robot_block[ni][nj] == ' '          -> déplacement simple :
                 successeur = deepcopy(self)
                 successeur.robot_block[ri][rj] = ' '
                 successeur.robot_block[ni][nj] = 'R'
                 successeur.robot_position = (ni, nj)

            3. Si robot_block[ni][nj] == 'B'          -> tentative de poussée :
                 (bi, bj) = (ni + di, nj + dj)       # case derrière la caisse
                 Valide seulement si wall_space_obstacle[bi][bj] != 'O'
                                 ET robot_block[bi][bj] == ' '   (pas de 2e caisse)
                 Sinon invalide. Si valide :
                     successeur = deepcopy(self)
                     successeur.robot_block[bi][bj] = 'B'
                     successeur.robot_block[ni][nj] = 'R'
                     successeur.robot_block[ri][rj] = ' '
                     successeur.robot_position = (ni, nj)

            4. Pour un mouvement valide : ajouter (action, successeur) à la liste.

        Attention : ne JAMAIS modifier self (on travaille sur la copie),
        et ne jamais toucher à wall_space_obstacle.
        """
        raise NotImplementedError
