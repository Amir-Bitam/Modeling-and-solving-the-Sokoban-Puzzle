"""
search.py : algorithmes de recherche (pour l'instant : BFS uniquement).
"""

from queue import Queue

from node import Node


class Search:

    # ------------------------------------------------------------------
    # MEMBRE 3
    # ------------------------------------------------------------------
    @staticmethod
    def breadthFirst(initial_node):
        """
        Recherche en largeur (BFS), selon le pseudo-code du cours.

        Entrée  : initial_node (Node dont le state est l'état initial)
        Sortie  : (goal_node, nb_etapes)   si une solution est trouvée
                  (None, nb_etapes)        sinon

        TODO :
            1. Si initial_node.state.isGoal() -> return initial_node, 0

            2. open   = Queue()  (FIFO)      ; open.put(initial_node)
               closed = set()                ; ensemble des ÉTATS déjà développés
               in_open = {initial_node.state}  ; ensemble parallèle pour tester
                                                 "déjà dans Open" en O(1)
               (possible grâce à __eq__ / __hash__ de SokobanPuzzle)

            3. step = 1
               tant que True :
                   a. si open.empty() -> return None, step
                   b. current = open.get()
                      in_open.discard(current.state)
                      closed.add(current.state)
                   c. pour (action, successor) dans current.state.successorFunction() :
                          child = Node(successor, current, action)
                          si child.state.isGoal() -> return child, step
                          si child.state pas dans closed ET pas dans in_open :
                              open.put(child)
                              in_open.add(child.state)
                   d. step += 1

            4. Afficher la progression est optionnel
               (ex : print(f"*** Step {step} ***") comme dans le code de la prof,
                mais c'est lent sur les gros niveaux).
        """
        raise NotImplementedError
