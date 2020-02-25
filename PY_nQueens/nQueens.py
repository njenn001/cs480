import numpy as mp 
import math 
import random

#############
#Class to represent each of the queen pieces 
class Queen:
    def __init__(self):
        self.id = 0
        self.attacking = [] 
        self.safe = True
#############

#############
#Class to represenet each space 
class Space: 
    def __init__(self, i): 
        self.index = i 
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
#Function implementing a Hill Climbing Search on a 8x8 board
def eightBy(): 
    row_col = 8 
    num_q = 8 
    board = Board(row_col, row_col)

    for x in range( row_col*row_col ): 
        board

#############

#############

def sixteenBy():
    row_col = 16
    num_q = 16
    board = Board(row_col, row_col)

    
#############

#############

def thirtytwoBy():
    row_col = 32 
    num_q = 32
    board = Board(row_col, row_col)

    x = random.uniform 
    y = 0

    xnot = getNewRand(x)

    i = 0
    while i < 100: 
        i+= 1
        



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

def getNewRand(x): 
    y = 0.0 

    while y <= .1: 
        y = round(random.uniform(0,1) + x, 1)
        print(y) 
        
    return (y)

def main(): 

    MAX_STEP = 1.0

    eightBy() 
    sixteenBy()
    thirtytwoBy() 


    

if __name__ == "__main__":
    main()