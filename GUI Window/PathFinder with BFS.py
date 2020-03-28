**********************************************
# Path-Finder with BFS

# Implemented on Turtle GUI
# Python : 3.7

# Prashanth Umapathy
# 29/3/2020

**********************************************

import turtle
import time 
import sys
from queue import deque

db = turtle.Screen()
db.bgcolor('Black')
db.title('BFS Path-Finder')
db.setup(1300,700)

# Maze Class and its attributes
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

# When the final path is found
class Finish(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('green')
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('red')
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed(0)

# grid1 = [
# "+++++++++++++++",
# "+s+       + +e+",
# "+ +++++ +++ + +",
# "+ + +       + +",
# "+ +   +++ + + +",
# "+ + + +   + + +",
# "+   + +   + + +",
# "+++++ +   + + +",
# "+     +   +   +",
# "+++++++++++++++",
# ]

# grid2 = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

# grid3 = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]


grid4 = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++f+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

# setting up classes
maze = Maze()
red = Red()
blue = Blue()
finish = Finish()
yellow = Yellow()

# setting up lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}  

def main_Maze(grid):
    global start_x, start_y, end_x, end_y

    for y in range(len(grid4)):
        for x in range(len(grid[y])):
            legend = grid[y][x]
            screen_x = -600 + (x * 24)
            screen_y = 288 - (y * 24)

            if legend == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))
            
            if legend == " " or legend == "f":
                path.append((screen_x, screen_y))

            if legend == "f":
                finish.color('purple')
                finish.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                finish.stamp()
                finish.color('green')
            
            if legend == 's':
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x,screen_y)

def killProcess():
    # db.exitOnClick()
    sys.exit()

def find(x,y):
    frontier.append((x,y))
    solution[x,y] = x,y

    while len(frontier) > 0:        # exit while loop when frontier queue equals zero
        time.sleep(0)
        x,y = frontier.popleft()    # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:   # check the cell on the left
            cell = (x-24, y)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x - 24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:   # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        finish.goto(x,y)
        finish.stamp()

def backTracking(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while(x, y) != (start_x, start_y):  # stop loop when current cells == start cell
        yellow.goto(solution[x, y])     # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]           # "key value" now becomes the new key
    time.sleep(5)

if __name__ == "__main__":              # Main Program starts here
    main_Maze(grid4)
    find(start_x, start_y)
    backTracking(end_x, end_y)
    killProcess()
    
