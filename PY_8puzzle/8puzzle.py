import numpy as np
import random
import math 
import collections
import queue 
from queue import Queue

#CLASS TO REPRESENT THE GOAL STATE 
class GoalState:
    def __init__(self, r, c):
        self.puzzle = []
        p = np.arange(r*c)

        for i in range(len(p)):
            self.puzzle.append(int(p[i]))

#CLASS TO REPRESENT THE STATE OF EACH OF THE NODES
class State: 
    def __init__(self, mat):
        self.mat = mat
        
        self.visited = False

#CLASS TO REPRESENT THE NODES CREATING THE BRANCHES TO THE GOAL STATE 
class Node: 
    def __init__(self, state):
        self.state = state
        self.parent = []
        self.children = []

#CLASS TO REPRESENT THE ENTIRE BOARD 
class Matrix:
    def __init__(self, r, c, cells):
        
        self.rows = r
        self.columns = c           
        self.cells = cells

        def setBox( box ):
            self.blank = box

#CLASS TO REPRESENT EACH SQUARE 
class Box: 
    def __init__(self, val, index):
        self.value = val 
        self. id = index
        self.moves = [] 

#############
#FUNCTION TO MOVE THE BLANK TILE UP
def move_up( temp, idnt ):
    num = 0 
    new = temp
    for i in temp:
        num = num + 1

    row_col = int(math.sqrt(num))
    cvalue = temp[idnt - row_col]
    new[idnt - row_col] = 0 
    new [idnt] = cvalue

    return new

#############
#FUNCTION TO MOVE THE BLANK TILE DOWN 
def move_down( temp, idnt ):
    num = 0
    new = temp
    for i in temp:
        num = num + 1

    row_col = int(math.sqrt(num))
    cvalue = temp[idnt + row_col]
    new[idnt + row_col] = 0 
    new [idnt] = cvalue

    return new

#############
#FUNCTION TO MOVE THE BLANK TILE TO THE LEFT 
def move_left( temp, idnt ):
    num = 0
    new = temp
    for i in temp:
        num = num + 1

    row_col = int(math.sqrt(num))
    cvalue = temp[idnt - 1]
    new[idnt - 1] = 0 
    new [idnt] = cvalue

    return new

#############
#FUNCTION TO MOVE THE BLANK TILE TO THE RIGHT 
def move_right( temp, idnt ):
    num = 0
    new = temp
    for i in temp:
        num = num + 1

    row_col = int(math.sqrt(num))
    cvalue = temp[idnt + 1]
    new[idnt + 1] = 0 
    new [idnt] = cvalue

    return new

#############
#FUNCTION TO PREFORM THE MOVE AND POPULATE THE QUEUE 
def makeMoves( state, q, states, node ): 
    #print ( "Making Moves...\n" )

    for i in state.mat.blank.moves: 
        #print ( i ) 

        if (i == 'D'):
            new = []
            temp = []
            temp = state.mat.cells.copy()
            idnt = state.mat.blank.id 
            new = move_down(temp, idnt)
            #print (new, end = "")
            num = 0 
            for i in temp:
                num = num + 1
        
            row_col = int(math.sqrt(num))
            nmat = Matrix(row_col, row_col, new)
            nmat.cells = new.copy()
            nstat = State(nmat)
            nstat.visited = True 

            visited = False
            for s in states:
                if nstat.mat.cells == s.mat.cells:
                    #print ("Duplicate")
                    visited = True 

            if not visited:
                nNode = Node(nstat)
                nNode.parent.append(node)
                q.put(nNode)
                node.children.append(nNode) 
                #display_board(nstat.mat)

        elif (i == 'U'):
            temp = []
            new = []
            temp = state.mat.cells.copy()
            idnt = state.mat.blank.id 
            new = move_up(temp, idnt)
            #print (new, end = "")
            num = 0 
            for i in temp:
                num = num + 1
        
            row_col = int(math.sqrt(num))
            nmat = Matrix(row_col, row_col, new)
            nmat.cells = new.copy()
            nstat = State(nmat)
            nstat.visited = True

            visited = False
            for s in states:
                if nstat.mat.cells == s.mat.cells:
                    #print ("Duplicate")
                    visited = True 

            if not visited:
                nNode = Node(nstat)
                nNode.parent.append(node)
                q.put(nNode)
                node.children.append(nNode) 
                #display_board(nstat.mat)

        elif (i == 'L'): 
            temp = []
            new = []
            temp = state.mat.cells.copy()
            idnt = state.mat.blank.id 
            new = move_left(temp, idnt)
            #print (new, end = "")
            num = 0 
            for i in temp:
                num = num + 1
        
            row_col = int(math.sqrt(num))
            nmat = Matrix(row_col, row_col, new)
            nmat.cells = new.copy()
            nstat = State(nmat)
            nstat.visited = True

            visited = False
            for s in states:
                if nstat.mat.cells == s.mat.cells:
                    #print ("Duplicate")
                    visited = True 

            if not visited:
                nNode = Node(nstat)
                nNode.parent.append(node)
                q.put(nNode)
                node.children.append(nNode) 
                #display_board(nstat.mat)

        elif (i == 'R'):
            temp = []
            new = []
            temp = state.mat.cells.copy()
            idnt = state.mat.blank.id 
            new = move_right(temp, idnt)
            #print (new, end = "")
            num = 0 
            for i in temp:
                num = num + 1
        
            row_col = int(math.sqrt(num))
            nmat = Matrix(row_col, row_col, new)
            nmat.cells = new.copy()
            nstat = State(nmat)
            nstat.visited = True

            visited = False
            for s in states:
                if nstat.mat.cells == s.mat.cells:
                    #print ("Duplicate")
                    visited = True

            if not visited:
                nNode = Node(nstat)
                nNode.parent.append(node)
                q.put(nNode)
                node.children.append(nNode) 
                #display_board(nstat.mat)
#############

#############
#FUNCTION TO COMPARE THE CURRENT STATE WITH THE GOAL STATE 
def checkGoal( state, goal ):

    if (state.mat.cells == goal.puzzle):
        return True
    else:
        return False
#############

#############
#FUNCITON THAT IMPLEMENTS THE BREADTH FIRST SEARCH ALGORITHM 
def BreadthFirst( state, goal, fifo ):
    print ("\nBreadth-First Search... ")
    print ( "Finding Solution...\n" )  
    
    states = []

    fifo.put(Node(state))

    while True: 
        
        node = fifo.get(0) 

        nstate = node.state 
        states.append(nstate)

        check = checkGoal(nstate, goal)

        if (check): 
            print ("Solution Found!!! \n")
            return node

        check_moves(nstate.mat)                
        makeMoves ( nstate, fifo, states, node )             
        
        #print (len(list(fifo.queue)))                
#############



#############
#FUNCTION TO ASSIGN POSSIBLE MOVES TO EACH BOX 
def check_moves( board ):

    #print ("\nChecking possible moves ... \n")

    for i in range(len(board.cells)):
       
        if board.cells[i] == 0: 
            tile = Box(0, i)
    
    if (tile.id - 1) >= 0 or tile.id == 0:

        if tile.id + board.columns < (board.rows * board.columns): 
            tile.moves.append('D')

        if tile.id - board.columns >= 0: 
            tile.moves.append('U')

        if (tile.id) % board.columns != 0:
            tile.moves.append('L')

        if (tile.id + 1) % board.columns != 0:
            tile.moves.append('R')

    board.blank = tile 

    #print (tile.moves)
#############

#############
#CUSTOM FUNCTION TO DISPLAY THE BOARD
def display_board( board ):

    print ("------" * board.columns)

    for i in range(board.columns * board.rows):

        if i % board.columns == 0 and i != 0: 
            print ("\n" + "| " + str(board.cells[i]) + " |-", end = "")
        elif i % board.columns == 0 and i == 0: 
            print ("| " + str(board.cells[i]) + " |-", end = "")
        else:
            print ("| " + str(board.cells[i]) + " |-", end = "")

    print ("\n" + ("------" * board.columns))
#############

#############
#FUNCTION USED TO GATHER INPUT ARRAY FROM THE USER
def getArray():
        
    nList = [] 
    rList = [] 
    while True:
        try:             
            
            F = open(input(str("\nEnter file name containing the initial array...\nText File: ")),"r")
            
            nList = F.read().split(' ')

            for i in range(len(nList)):
                rList.append(int(nList[i]))

            break
        except Exception as ex:
            print("Invalid Input")
            print (ex)  
            continue

    return rList
#############

#############
#FUNCTION THAT PROMPTS THE USER FOR THE MATRIX FILE AND SEARCH ALGORITHM 
def main():


    fifo = queue.Queue(0)
    lifo = queue.LifoQueue(0)

    m = getArray()

    counter = 0
    for i in m: 
        counter = counter + 1

    row_col = int(math.sqrt(counter))

    mat = Matrix(row_col, row_col, m)
    display_board(mat)
    goal = GoalState(row_col, row_col)
 
    print ("\nChoose a search pattern:")
    print ("\n1) Breadth-first \n2) Depth-first")
    
    while True:
        try:
            choice = int (input("Choice: "))
        except Exception as ex: 
            print ("Not the correct input type")
            continue
    
        if choice == 1:
            check_moves( mat )
            state = State ( mat ) 
            state.visited = True
            #print ("Breadth-first")

            result = BreadthFirst( state, goal, fifo )

            if result == None:
                print ("No solution found")
            else:
                print ("Path:\n")

                while (len(result.parent) >= 0): 

                    if (len (result.parent) != 0):
                        display_board (result.state.mat)
                        result = result.parent[0]
                    elif (len (result.parent) == 0):
                        display_board (result.state.mat)
                        break

                #display_board(result.state.mat)
                
            break

        elif choice == 2:
            print ("Depth-first")

            display_board(mat)
            break 

        else:
            print ("Choose a search pattern (1 or 2):")
            continue 
#############

if __name__ == "__main__":
    main() 