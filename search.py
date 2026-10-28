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

    
        heapq.heappush(open_list, (initial_node.f, counter, initial_node))

        if initial_node.state.isGoal():
            return (initial_node, 0)

        while open_list:
            _, _, current = heapq.heappop(open_list)

            if current.g > closed[current.state]:
                continue

            steps = steps + 1

            if current.state.isGoal():
                return (current, steps)

            for action, successor_state in current.state.successorFunction():
                child = Node(successor_state, current, action)

                if child.state not in closed or child.g < closed[child.state]:

                    child.setF(heuristic)
                    counter += 1
                    heapq.heappush(open_list, (child.f, counter, child))
                    closed[child.state] = child.g
                                
        return (None, steps)


