from collections import deque
from node import Node


class Search:
    
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

    


