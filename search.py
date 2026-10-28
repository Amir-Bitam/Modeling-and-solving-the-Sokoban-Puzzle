from collections import deque
from node import Node
import heapq



class Search:


    # ------------------------------------------------------------------
    # Noufel
    # ------------------------------------------------------------------

    
    @staticmethod 
    def breadthFirst(initial_node):
        steps= 0
        open_list = deque([initial_node])
        open_listset= {initial_node.state}
        closed = set()

        

        if initial_node.state.isGoal():
            return (initial_node , 0)

        while open_list:
            current = open_list.popleft()
            open_listset.remove (current.state)
            closed.add(current.state)
            steps= steps+1


            for action, successor_state in current.state.successorFunction():

                

                child = Node(successor_state,current,action)
                if child.state.isGoal():  return (child ,steps)

                if child.state not in closed and child.state not in open_listset:
                    open_list.append(child)
                    open_listset.add(child.state)

        return (None,steps)

    @staticmethod
    def aStar(initial_node, heuristic):
        initial_node.setF(heuristic)

        steps = 0
        open_list = []
        closed = {initial_node.state: initial_node.g} #kind of like the close list it holds the nodes with the best costs 
        counter = 0

    
        heapq.heappush(open_list, (initial_node.f, counter, initial_node)) # placer noeud initiale dans le tas

        if initial_node.state.isGoal(): #i noeud initial is gal, we stop
            return (initial_node, 0)

        while open_list: #tant que there are still des noeud a explorer
            _, _, current = heapq.heappop(open_list) # recuperer noeud avec le plus petit f

            if current.g > closed[current.state]: #Si ce nœud possède un coût plus grand que le meilleur coût déjà enregistré pour le même état, il est ignoré.
                continue

            steps = steps + 1 #compte le nombre de nœuds retirés du tas et développés.

            if current.state.isGoal(): 
                return (current, steps)

            for action, successor_state in current.state.successorFunction(): #generation des enfants. chaque move produit un enfant
                child = Node(successor_state, current, action)

                if child.state not in closed or child.g < closed[child.state]:

                    child.setF(heuristic)
                    counter += 1
                    heapq.heappush(open_list, (child.f, counter, child))
                    closed[child.state] = child.g
                                
        return (None, steps)


