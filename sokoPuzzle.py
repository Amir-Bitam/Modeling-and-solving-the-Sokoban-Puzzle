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

from copy import copy


class SokobanPuzzle:

    # Action -> déplacement (ligne, colonne). CONTRAT : ne pas changer les clés.
    DIRECTION = {
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

    def _clone(self):
        new_state = copy(self) 
        new_state.robot_block = [row[:] for row in self.robot_block]
        return new_state

    def successorFunction(self):
        successors = []
        ri, rj = self.robot_position #get robot_position from self

        for action in self.moves:
            x, y = self.DIRECTION[action] #get how much this move is gonna affect the robot position
            ni, nj = ri + x, rj + y #calculate next position


            #if next position is a wall, skip to next action
            if self.wall_space_obstacle[ni][nj] == 'O': 
                continue

            #if next position is a box, we move box to the same direction
            if self.robot_block[ni][nj] == 'B':
                nbi , nbj = ni + x, nj + y #calculate next box position

                if self.wall_space_obstacle[nbi][nbj] == 'O' or self.robot_block[nbi][nbj] == 'B':
                    continue #if next box position is a wall or another box, move invalid, skip to next action

                #else, move is valid, we make a clone of the state

                new_state = self._clone()
                new_state.robot_block[nbi][nbj] = 'B' #move the box in the clone

            else: #if its not a box, it means its a free cell
                new_state = self._clone()

            #by the end of this if-else statement we have a clone of the state (either with a moved box or without) in both cases we have to move the robot

            new_state.robot_block[ri][rj] = ' ' #old position becomes empty cell
            new_state.robot_block[ni][nj] = 'R' #move robot to new position
            new_state.robot_position = (ni, nj) #update robot position for new state

            successors.append((action, new_state))

        return successors
