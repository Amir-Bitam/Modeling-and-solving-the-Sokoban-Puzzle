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
    def aStar(initial_node,heuristic):
        initial_node.setF(heuristic)

        steps= 0
        open_list = []
        counter = 0 
        open_listset= {initial_node.state}
        closed = set()
        heapq.heappush(open_list, (initial_node.f, counter, initial_node))
        

        if initial_node.state.isGoal():
            return (initial_node , 0)

        while open_list:
            _, _, current = heapq.heappop(open_list)
            open_listset.remove(current.state)
            closed.add(current.state)
            steps= steps+1


            for action, successor_state in current.state.successorFunction():

                

                child = Node(successor_state,current,action)
                if child.state.isGoal():  return (child ,steps)

                if child.state not in closed and child.state not in open_listset:
                    child.setF(heuristic)
                    counter +=1
                    heapq.heappush(open_list,(child.f,counter,child))
                    open_listset.add(child.state)

        return (None,steps)
    


