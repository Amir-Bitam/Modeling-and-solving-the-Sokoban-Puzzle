class Node:

    # ------------------------------------------------------------------
    # Noufel
    # ------------------------------------------------------------------

    def __init__(self,state,parent = None ,action="",  c = 1):
        self.state = state
        self.parent = parent
        self.action = action

        if parent is None:
            self.g = 0
        else:
            self.g = parent.g + c  

    def getPath(self):
        current = self
        path = [] 
        while current is not None:
            path.append(current.state)
            current = current.parent     

        path = path[::-1]
        return path

    def getSolution(self):
        current = self
        path = [] 
        while current.parent is not   None:
            path.append(current.action)
            current = current.parent     

        path = path[::-1]
        return path
