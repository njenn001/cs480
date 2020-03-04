import numpy as np 

##########
#Class to represent the entire board
class Column: 
    def __init__(self):
        self.col = [] 


##########
#Class to represent the entire board
class Board(): 
    def __init__(self):
        self.r = 9 
        self.c = 9 
        self.cols = [] 
        self.rows = [] 

        self.puzzle = np.zeros(shape=(self.r,self.c))

##########
#Function to read starting board from text file
def loadBoard(fname): 
    print(fname)


def main(): 

    while True: 
        try:
            f = open(input("Enter puzzle text file: "), "a")

            loadBoard(f)

            break
        except Exception as ex: 
            print(ex) 
            continue

    board = Board() 

    print(board.puzzle)


    

if __name__ == "__main__":
    main() 