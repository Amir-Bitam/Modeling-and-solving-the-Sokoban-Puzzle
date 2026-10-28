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

from collections import deque
from copy import deepcopy
from itertools import permutations

class SokobanPuzzle:

    # Action -> déplacement (ligne, colonne). CONTRAT : ne pas changer les clés.
    DIRECTION = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    # ------------------------------------------------------------------
    # Amir
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
    # Amel
    # ------------------------------------------------------------------

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

                new_state = deepcopy(self)
                new_state.robot_block[nbi][nbj] = 'B' #move the box in the clone

            else: #if its not a box, it means its a free cell
                new_state = deepcopy(self)

            #by the end of this if-else statement we have a clone of the state (either with a moved box or without) in both cases we have to move the robot

            new_state.robot_block[ri][rj] = ' ' #old position becomes empty cell
            new_state.robot_block[ni][nj] = 'R' #move robot to new position
            new_state.robot_position = (ni, nj) #update robot position for new state

            successors.append((action, new_state))

        return successors

    def h1(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.wall_space_obstacle[i][j] != 'S':
                    if self.robot_block[i][j] == 'B':
                        count += 1
        return count

    def h2(self):

        UnplacedBoxes =  deque([])
        GoalSpots = deque([])
        
        for i in range(self.height):
            for j in range(self.width):
                if self.wall_space_obstacle[i][j] != 'S':
                    if self.robot_block[i][j] == 'B':
                      UnplacedBoxes.append((i,j))  
                else:
                    if self.robot_block[i][j] != 'B':
                        GoalSpots.append((i,j))

        #bon hna dert fonction dakhel fonction besh le code il est un peu comprehensible 

        def manhattan_distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        total = 0
        for box in UnplacedBoxes:
            min_dist = min(manhattan_distance(box, target) for target in GoalSpots)
            total += min_dist
        return 2 * self.h1() + total

    def h3(self):
        
        unplaced_boxes = []  # List that holds positions of boxes not on targets
        free_targets = [] # List that holds positions of free targets

        #boucle imbriquée that goes through each cell in the matrice and fills the two lists above
        for i in range(self.height):
            for j in range(self.width):
                if self.wall_space_obstacle[i][j] != 'S': 
                    if self.robot_block[i][j] == 'B': #if not target and box
                        unplaced_boxes.append((i, j))
                else:
                    if self.robot_block[i][j] != 'B': #if target and not box
                        free_targets.append((i, j))

        if not unplaced_boxes: # if all boxes are on targets, return 0
            return 0

        def manhattan_distance(pos1, pos2): # manhatten distance function
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        # permutations(free_targets) : generates all possible permutations of targets
        # for every permutation in permutations, we pair it with the list of boxes (assigns each target with each box in every permutation)
        # for each of those assignments, we calculate the manhatten distance between box and target
        # we sum the distances for each permutation and then take the min of them
        best_pushes = min(
            sum(manhattan_distance(box, target) for box, target in zip(unplaced_boxes, perm))
            for perm in permutations(free_targets)
        )

        robot = self.robot_position
        walk = min(manhattan_distance(robot, box) for box in unplaced_boxes) - 1 #it calculates the distance between the robot and each unplaced box, then takes the min distance

        #we add the walk distance to the min distance to push boxes to target
        return best_pushes + walk
        
