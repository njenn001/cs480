import numpy as np 
import math 
import random

#############
#Class to represent each of the queen pieces 
class Queen:
    def __init__(self):
        self.pos = 0 
        self.attacking = [] 
        self.safe = True
        self.moves = []
#############

#############
#Class to represenet each space 
class Space: 
    def __init__(self, i): 
        self.id = i 
        self.queen = None
        self.char = '-'

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
#Function to check the horizontal attacks 
def checkHorizontal(board, num_q, q): 

    print ("Horizontal")

############

#Function to check the vertical attacks 
def checkVertical(board, num_q, space): 
    print ("Queen Position: " + str(space.queen.pos))

    for i in range(num_q): 
        if i > 0: 
            if ((space.queen.pos - (i * num_q)) >  0 or (space.queen.pos - (i * num_q)) == 0):
                    space.queen.moves.append('U')
                    print (space.queen.moves) 
                #else:
                    #print ("Off Board")

    for i in range(num_q): 
        if i > 0: 
            if (space.queen.pos + (i * num_q)) <=  ((num_q * num_q) - 1):
                    space.queen.moves.append('D')
                    print (space.queen.moves) 
                #else:
                    #print ("Off Board")
            else: 
                break
 

############

#############
#Function to count the number of attacking queen pairs 
def countAttacks(board, num_q): 
    for x in board.spaces: 
        if  x.queen != None:
            
            checkVertical(board, num_q, x)
             

#############

#############
#Function to randomly place the queens in a space on the board 
def placeQueens(board, num_q): 
    rows = [] 
    i = 0
    while i < num_q: 
        
        while True: 
            if (i == 0):
                row = random.randint(0, num_q-1)
                
                used = False
                for y in rows:
                    if (row == y):
                        used = True
                
                if not used: 
                    rows.append(row)

                    nQ = Queen()
                    nQ.pos = row

                    board.spaces[row].queen = nQ 
                    board.spaces[row].char = 'Q'

                    #print ("[" + str(row) + "]")
                    break
                else: 
                    continue
            if (i == 1):
                row = random.randint(num_q, (num_q * 2 - 1))
                
                used = False
                for y in rows:
                    if (row == y):
                        used = True
                
                if not used: 
                    rows.append(row)    

                    nQ = Queen()
                    nQ.pos = row

                    board.spaces[row].queen = nQ 
                    board.spaces[row].char = 'Q'

                    #print ("[" + str(row) + "]")
                    break
                else: 
                    continue
            else:
                row = random.randint((num_q * i), (i * num_q) + (num_q - 1))
                
                used = False
                for y in rows:
                    if (row == y):
                        used = True
                
                if not used: 
                    rows.append(row)   

                    nQ = Queen()
                    nQ.pos = row

                    board.spaces[row].queen = nQ 
                    board.spaces[row].char = 'Q'

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
    
    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    placeQueens(board, num_q)
    display_board(board)
    countAttacks(board, num_q)


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
if __name__ == "__main__":
    main()
#############