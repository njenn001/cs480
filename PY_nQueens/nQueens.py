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
#############

#############
#Class to represenet each space 
class Space: 
    def __init__(self, i): 
        self.id = i 
        self.queen = None

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
#Function to count the number of attacking queen pairs 

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
        
    i = 0
    while i < num_q: 
        i+=1
        while True: 
            row = random.randint(0, 8)
            
            used = False
            for y in rows:
                if (row == y):
                    used = True
            
            if not used: 
                rows.append(row)
                #nQ
        
                print ("[" + str(row) + "]")
                break
            else: 
                continue
    
    display_board(board)
    

#############

#############

def sixteenBy():
    row_col = 16
    num_q = 16
    rows = [] 

    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    i = 0
    while i < num_q: 
        i+=1
        while True: 
            row = random.randint(0, 16)
            
            used = False
            for y in rows:
                if (row == y):
                    used = True
            
            if not used: 
                rows.append(row)
                #nQ
        
                print ("[" + str(row) + "]")
                break
            else: 
                continue
    
    display_board(board)
    
#############

#############

def thirtytwoBy():
    row_col = 32 
    num_q = 32
    rows = [] 

    board = Board(row_col, row_col)
    
    for x in range(row_col*row_col):
        space = Space(x)
        board.spaces.append(space) 
        #print (board.spaces[x].id) 
        
    i = 0
    while i < num_q: 
        i+=1
        while True: 
            row = random.randint(0, 32)
            
            used = False
            for y in rows:
                if (row == y):
                    used = True
            
            if not used: 
                rows.append(row)
                #nQ
        
                print ("[" + str(row) + "]")
                break
            else: 
                continue
    
    display_board(board)



#############

#############
#CUSTOM FUNCTION TO DISPLAY THE BOARD
def display_board( board ):

    print ("------" * int(board.cols / 2))

    i = 0 
    while i < len(board.spaces):
        if (i % board.cols != 0):
            print ("| " + str(board.spaces[i].id), end = " |")

        if (i % board.cols == 0 and i != 0):
            print ("\n" + "| " + str(board.spaces[i].id), end = " |")
        
        if (i % board.cols == 0 and i == 0):
            print ("| " + str(board.spaces[i].id), end = " |")

        i += 1
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