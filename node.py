"""
node.py : nœud de l'arbre de recherche.
"""


class Node:

    # ------------------------------------------------------------------
    # MEMBRE 3
    # ------------------------------------------------------------------
    def __init__(self, state, parent=None, action="", c=1):
        """
        state  : instance de SokobanPuzzle
        parent : nœud parent (None pour le nœud initial)
        action : action appliquée au parent pour obtenir ce nœud ("" pour la racine)
        c      : coût d'un pas (toujours 1 ici)
        g      : coût du chemin = 0 si pas de parent, sinon parent.g + c

        TODO : initialiser self.state, self.parent, self.action, self.g
        """
        raise NotImplementedError

    def getPath(self):
        """
        Retourne la liste des ÉTATS de l'état initial jusqu'à l'état but.

        TODO :
            - partir de self, remonter via .parent jusqu'à None
              en ajoutant node.state à une liste
            - retourner la liste inversée ([::-1])
        """
        raise NotImplementedError

    def getSolution(self):
        """
        Retourne la liste des ACTIONS appliquées depuis l'état initial pour
        atteindre l'état but, ex : ["R", "U", "L", "L"].

        TODO :
            - même remontée que getPath, mais en collectant node.action
            - ne PAS inclure l'action "" du nœud racine
            - retourner la liste inversée
        """
        raise NotImplementedError
