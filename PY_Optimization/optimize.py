import math 
import random 

def eggHolderFunction(x,y): 
    print(x)
    print(y)

    return (-(y+47)*math.sin(math.sqrt(abs((x/2.0) + (y+47)))) -
        x*math.sin(math.sqrt(abs(x-(y+47))))) 


def main(): 
    print ("Egg Holder Function Optimization")

    x = random.randint(-10000, 10000)
    y = random.randint(-10000, 10000)

    cost = eggHolderFunction(x,y)

    print (cost)

    

if __name__ == "__main__":
    main()