from queue import PriorityQueue

class State(object):

    def __init__(self, value, parent,start = 0,goal = 0):
        # Parameters for the final path

        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            # Incase path is craeted, append it to current path
            self.start  = parent.start
            self.goal   = parent.goal
            self.path   = parent.path[:]
            self.path.append(value)
        else:
            # Incase no path is created already
            self.path   = [value]
            self.start  = start
            self.goal   = goal

    def GetDistance(self):
        pass

    def CreateChildren(self):
        pass

class State_String(State):
    #base class
    def __init__(self,value,parent,
                 start = 0,
                 goal = 0):

        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDistance()

    def GetDistance(self):
        # If destination reached

        if self.value == self.goal:
            return 0
        dist = 0
        
        # If not, keep adding the path

        for i in range(len(self.goal)):
            letter = self.goal[i]
            try:
                dist += abs(i - self.value.index(letter))
            except:
                dist += abs(i - self.value.find(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            # Many permutations for the val, that's it
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    # The Algorithm Part
    def __init__(self, start , goal):
        self.path          = []
        self.visitedQueue  = []
        self.priorityQueue = PriorityQueue()
        self.start         = start
        self.goal          = goal

    def Solve(self):
        startState = State_String(self.start,0,self.start,self.goal)

        # The function carrying out the algo

        count = 0
        self.priorityQueue.put((0,count,startState))

        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)

            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count +=1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist,count,child))

        if not self.path:
            print("Goal of %s is not possible!" % (self.goal))

        return self.path


if __name__ == "__main__":
    
    # Pass the values
    start1 = input("Enter the initial version: ")
    goal1  = input("Enter the final version: ")
    print("Solving...")

    a = AStar_Solver(start1, goal1)
    a.Solve()

    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))
