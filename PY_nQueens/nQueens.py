import numpy as mp 
import math 

#############
#Class to represent each of the queen pieces 
class Queen:
    def __init__(self):
        self.id = 0
        self.moves = [] 
        self.safe = True
#############

#############
#Class to represent the entire board
class Board: 
    def __init__(self, r, c): 
        self.rows = r
        self.cols = c 
        self.queens = [] 
        self.attacking = 0 
#############

#############
#Function implementing a Hill Climbing Search on a 8x8 board
def eightBy(): 
    row_col = 8 
    num_q = 8 
    board = Board(row_col, row_col)


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

def main(): 

    eightBy() 
    sixteenBy()
    thirtytwoBy() 


    

if __name__ == "__main__":
    main()