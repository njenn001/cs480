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
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator 
        self.depth = 0 

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
def makeMoves( state, q ): 
    print ( "Making Moves" )

    for i in state.mat.blank.moves: 
        print ( i ) 

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
            q.put(nstat)

            display_board(nstat.mat)

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
            q.put(nstat)
            
            display_board(nstat.mat)

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
            q.put(nstat)
            
            display_board(nstat.mat)

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
            q.put(nstat)
            
            display_board(nstat.mat)


#############


def checkState( stateA, checkState ):
    sA = [] 
    cS = [] 
    for i in stateA.mat:
        sA.append(stateA[i]) 
        cS.append(checkState[i])

    if (sA == cS): 
        print ("Visited")



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
    print ("BFS")

    fifo.put(state)

    check = checkGoal( state, goal )
    
    if (check):
        print ( "Solution Found" )
        sols = [] 
        return sols

    else:
        while True: 
            print ( "Finding Solution" )  
            
            nstate = State(fifo.get(0).mat)
              
            makeMoves ( nstate, fifo ) 
            loop = 0  
            for i in list(fifo.queue): 
                loop = loop + 1 

                display_board(i.mat)
                print (loop * 25)

                check_moves(i.mat)
                check = checkGoal(i, goal)

                if (check):
                    print ( "Solution Found" )
                    break
                else: break
            break

    """
    nodes = []
    nodes.append( Node( board.cells, None, None, 0) )

    while True:
        if len( nodes ) == 0: return None

        node = nodes[0]
        nodes.pop(0)

        if collections.Counter(node.state) == collections.Counter(goal):
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operator)
                if temp.depth == 1: break
                temp = temp.parent
            return moves				

        nodes.extend( expand_node( node, nodes ) )

    """

#############



#############
#FUNCTION TO ASSIGN POSSIBLE MOVES TO EACH BOX 
def check_moves( board ):

    print ("\nChecking possible moves ... \n")

    for i in range(len(board.cells)):
       
        if board.cells[i] == 0: 
            tile = Box(0, i)
            print (i)
    
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

    print (tile.moves)
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
            display_board( mat )
            state = State ( mat ) 
            state.visited = True
            #print ("Breadth-first")

            result = BreadthFirst( state, goal, fifo )

            if result == None:
                print ("No solution found")
            elif result == [None]:
                print ("Start node was the goal!")
            else:
                print (result)
                print (len(result), " moves")

            #
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