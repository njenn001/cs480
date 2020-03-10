import numpy as np 
import math 
import random

#############
#Class to represent each node State 
class State: 
    def __init__(self):
        self.board = None 

#############

#############
#Class to represent each of the queen pieces 
class Queen:
    def __init__(self):
        self.pos = 0 
        self.attacking = [] 
        self.safe = False
        self.moves = []

#############

#############
#Class to represenet each space 
class Space: 
    def __init__(self, i): 
        self.id = i 
        self.queen = None
        self.char = '-'
        self.attacking = 0 

#############

#############
#Class to represent the entire board
class Board: 
    def __init__(self, r, c): 
        self.rows = r
        self.cols = c 
        self.spaces = []
        self.attacking = 0 
        
#############

#############
#Function to count the horizontal attacks 
def checkDiagonal(board, num_q, space): 
    #print("check Diagonal")

    ### Left Down Diagonal
    y = 1
    while y < num_q: 

        ### Auto break if space is on right edge 
        if ((space.id) % num_q == 0): 
            #print ("Auto Break")
            break
        
        ### Left Down diagonal
        if ((space.id + ((y*num_q) - y)) % num_q == 0):
            if (space.id + ((y*num_q) - y) <= ((board.rows * board.cols) - 1)): 
                if board.spaces[space.id + ((y*num_q) - y)].queen != None: 
                    #print ("attacking LD")
                    space.queen.attacking.append(board.spaces[space.id + ((y*num_q) - y)].queen)
                    break 
            break
        if (space.id + ((y*num_q) - y) <= ((board.rows * board.cols) - 1)): 
            if board.spaces[space.id + ((y*num_q) - y)].queen != None: 
                #print ("attacking LD")
                space.queen.attacking.append(board.spaces[space.id + ((y*num_q) - y)].queen)
                
        y += 1

    ### Left Up Diagonal
    y = 1
    while y < num_q: 

        ### Auto break if space is on right edge 
        if ((space.id) % num_q == 0): 
            #print ("Auto Break")
            break
        
        ### Left Up diagonal
        if ((space.id - (y + (y*num_q))) % num_q == 0):
            if (space.id - (y + (y*num_q)) >= 0): 
                if board.spaces[space.id - (y + (y*num_q))].queen != None: 
                    #print ("attacking LU")
                    space.queen.attacking.append(board.spaces[space.id - (y + (y*num_q))].queen)
                    break 
            break
        if (space.id - (y + (y*num_q)) >= 0): 
            if board.spaces[space.id - (y + (y*num_q))].queen != None: 
                #print ("attacking LU")
                space.queen.attacking.append(board.spaces[space.id - (y + (y*num_q))].queen)
                
        y += 1
    
    ### Right Down Diagonal
    y = 1
    while y < num_q: 

        ### Auto break if space is on right edge 
        if ((space.id + 1) % num_q == 0): 
            #print ("Auto Break")
            break
        
        ### Right Down diagonal
        if ((space.id + (y + (y*num_q)) + 1) % num_q == 0):
            if (space.id + (y + (y*num_q)) <= ((board.rows * board.cols) - 1)): 
                if board.spaces[space.id + (y + (y*num_q))].queen != None: 
                    #print ("attacking RD")
                    space.queen.attacking.append(board.spaces[space.id + (y + (y*num_q))].queen)
                    break 
            break
        if (space.id + (y + (y*num_q)) <= ((board.rows * board.cols) - 1)): 
            if board.spaces[space.id + (y + (y*num_q))].queen != None: 
                #print ("attacking RD")
                space.queen.attacking.append(board.spaces[space.id + (y + (y*num_q))].queen)
                
        y += 1

    ### Right Up Diagonal 
    y = 1 
    while y < num_q:

        ### Auto break if space is on right edge 
        if ((space.id + 1) % num_q == 0): 
            #print ("Auto Break")
            break
        
        ### Right Up diagonal
        if ((space.id - ((y*num_q) - y) + 1) % num_q == 0):
            if (space.id - ((y*num_q) - y) > 0): 
                if board.spaces[space.id  - ((y*num_q) - y)].queen != None: 
                    #print ("attacking RU")
                    space.queen.attacking.append(board.spaces[space.id - ((y*num_q) - y)].queen)
                    break 
            #print ("sum")
            break

        if (space.id - ((y*num_q) - y) > 0 ): 
            if board.spaces[space.id  - ((y*num_q) - y)].queen != None: 
                #print ("attacking RU")
                space.queen.attacking.append(board.spaces[space.id  - ((y*num_q) - y)].queen)

        y += 1  

#############

#############
#Function to count the horizontal attacks 
def checkVertical(board, num_q, space): 
    #print("check vetical")

    for i in range(num_q): 
        if i > 0: 
            if (space.id + (i*8) <= ((board.rows * board.cols) - 1)): 
                if board.spaces[space.id + (i*8)].queen != None: 
                    #print ("attacking")
                    space.queen.attacking.append(board.spaces[space.id + (i*8)].queen)

    for i in range(num_q): 
        if i > 0: 
            if (space.id - (i*8) >= 0): 
                if board.spaces[space.id - (i*8)].queen != None: 
                    #print ("attacking")
                    space.queen.attacking.append(board.spaces[space.id - (i*8)].queen)

#############

#############
#Function to count the horizontal attacks 
def checkHorizontal(board, num_q, space): 
    #print("check horizontal")

    ### Left Horizontal 
    i = 0
    
    #print (space.id)

    while True: 
        i += 1 

        if (space.id - i) <= 0: 
            break
        
        if (space.id) % num_q == 0: 
            break 

        if (space.id - i) % num_q == 0: 
            if (board.spaces[space.id - i].queen != None): 
                #print ("L Q")
                space.queen.attacking.append(board.spaces[space.id - i].queen)

            break

        else: 
            if (board.spaces[space.id - i].queen != None): 
                #print ("L Q")
                space.queen.attacking.append(board.spaces[space.id - i].queen)

    ### Right Horizontal 
    i = 0

    while True: 
        i += 1 

        if (space.id + i) >= num_q * num_q: 
            break
        
        if (space.id + 1) % num_q == 0: 
            break 

        if ((space.id + i) + 1) % num_q == 0: 
            if (board.spaces[space.id + i].queen != None): 
                #print ("L Q")
                space.queen.attacking.append(board.spaces[space.id + i].queen)

            break

        else: 
            if (board.spaces[space.id + i].queen != None): 
                #print ("L Q")
                space.queen.attacking.append(board.spaces[space.id + i].queen)

#############

#############
#Function to check the moves  
def checkMoves(board, num_q, space): 
    #print ("Queen Position: " + str(space.queen.pos))

    ### Upward moves
    while True: 
        if (space.queen.pos - num_q) < 0: 
            #print ("First")
            break
            
        else:
            for i in range(num_q): 
                if (i > 0): 
                    if ((space.queen.pos - (i * num_q)) >  0 or (space.queen.pos - (i * num_q)) == 0):
                        if ( board.spaces[space.queen.pos - (i * num_q)].queen != None  ): 

                            #print (space.queen.pos - (i * num_q))
                            #print ("blocked")
                            
                            break
                        else: 

                            arr = []
                            arr.append('U')
                            arr.append(space.queen.pos - (i * num_q))
                            space.queen.moves.append(board.spaces[space.queen.pos - (i * num_q)].id)
            break

    ### Downward moves
    while True: 
        if (space.queen.pos + num_q) >= num_q * num_q: 
            #print ("Last")
            break 

        else:
            for i in range(num_q): 
                if (i > 0): 
                    if ((space.queen.pos + (i * num_q)) < num_q * num_q):
                        if ( board.spaces[space.queen.pos + (i * num_q)].queen != None  ): 

                            #print (space.queen.pos + (i * num_q))
                            #print ("blocked")
                            
                            break
                        else: 

                            arr = []
                            arr.append('U')
                            arr.append(space.queen.pos + (i * num_q))
                            space.queen.moves.append(board.spaces[space.queen.pos + (i * num_q)].id)
            break

    print (space.queen.moves) 
 
#############

#############
#Function to make a move 
def makeMove(board, states, costs): 
    i = 0
    for x in board.spaces: 
        
        if x.queen != None: 
            i += 1
            y = 0 

            for m in x.queen.moves:  
                y += 1
                x.queen.moves.pop(0)
                board.spaces[m].queen = x.queen
                x.queen = None
                x.char = "-"
                board.spaces[m].char = 'M' + str (i)
                #display_board(board)
                
                

                cost = countAttacks 

    display_board(board)
#############

#############
#Hill Climbing 
def hillClimbing (states): 

    cost = 0 
    costs = [] 
    while True: 
        b = states[len(states) - 1].board

        cost = b.attacking
        costs.append(cost)

        makeMove(b, states, costs)
        break

        

#############
#Function to count the number of attacking queen pairs 
def countAttacks(board, num_q): 
    for x in board.spaces: 
        if  x.queen != None:
            #print ("Queen Position: " + str(x.queen.pos))
            
            x.queen.attacking = [] 

            checkHorizontal(board, num_q, x) 
            checkVertical(board, num_q, x)
            checkDiagonal(board, num_q, x)
            """
            print ("Attacks:")
            if len(x.queen.attacking) != 0: 
                for y in x.queen.attacking: 
                    #print (y.pos)
            """
            board.attacking += len(x.queen.attacking)

    #print (str(board.attacking) + " attacks")

#############

#############
#Function to randomly place the queens in a space on the board (different cols)
def placeQueens(board, num_q): 
    
    
    rows = [] 
    cols = []
    i = 0
    while i < num_q: 
        
        while True: 
            
            col = random.randint(0, num_q - 1)
            row = random.randint(0, num_q - 1)    

            used = False
            for y in rows:
                if (row == y):
                    used = True
            
            user = False 
            for y in cols:
                if (col == y):
                    user = True

            if not used and not user:  
                rows.append(row)   

                nQ = Queen()
                nQ.pos = ( num_q * col ) + row

                board.spaces[( num_q * col ) + row].queen = nQ 
                board.spaces[( num_q * col ) + row].char = 'Q'

                #print ("[" + str(row) + "]")
                break
            else: 
                continue
        
        i+=1

#############

#############
#Function implementing a Hill Climbing Search on a 8x8 board
def eightBy(): 

    row_col = 8 
    num_q = 8 
    rows = [] 
    states = [] 

    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    placeQueens(board, num_q)
    
    display_board(board)

    for y in board.spaces: 
        if y.queen != None: 
            checkMoves(board, num_q, y)
    
    # count each pair of attacking queens 
    countAttacks(board, num_q) 

    # add initial state 
    nstate = State() 
    nstate.board = board 
    states.append(nstate)

    # start hill climbing 
    hillClimbing(states) 

    # choose which queen to move 
    #makeMove(board, num_q)

#############

#############
#Function implementing a Hill Climbing Search on a 16x16 board
def sixteenBy():
    row_col = 16
    num_q = 16
    rows = [] 

    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    placeQueens(board, num_q)
    display_board(board)

    for y in board.spaces: 
        if y.queen != None: 
            checkMoves(board, num_q, y)
    countAttacks(board, num_q)
    
#############

#############
#Function implementing a Hill Climbing Search on a 32x32 board
def thirtytwoBy():
    row_col = 32 
    num_q = 32
    rows = [] 

    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    placeQueens(board, num_q)
    display_board(board)

    for y in board.spaces: 
        if y.queen != None: 
            checkMoves(board, num_q, y)
    countAttacks(board, num_q)

#############

#############
#CUSTOM FUNCTION TO DISPLAY THE BOARD
def display_board( board ):

    print ("------" * int(board.cols / 2))

    i = 0 
    while i < len(board.spaces):
        if (i % board.cols != 0):
            print ("| " + str(board.spaces[i].char), end = " |")

        if (i % board.cols == 0 and i != 0):
            print ("\n" + "| " + str(board.spaces[i].char), end = " |")
        
        if (i % board.cols == 0 and i == 0):
            print ("| " + str(board.spaces[i].char), end = " |")

        i += 1

    print ("\n")
    print ("------" * int(board.cols / 2))
############# 

#############
#Main function to choose the size of the board
def main(): 

    MAX_STEP = 1.0

    print ("\nChoose a board size:")
    print ("\n1) 8x8 \n2) 16x16 \n3) 32x32")
        
    while True:
        try:
            choice = int (input("Choice: "))
        except Exception as ex: 
            print ("Not the correct input type")
            continue

        if choice == 1:
            print ("\n8x8 Chosen ...")
            eightBy()
            break

        if choice == 2:
            print ("\n16x16 Chosen ...")
            sixteenBy()
            break

        if choice == 3: 
            print ("\n32x32 Chosen ...")
            thirtytwoBy()
            break

        else:
            continue
#############

#############
#Calls the main function 
if __name__ == "__main__":
    main()
#############