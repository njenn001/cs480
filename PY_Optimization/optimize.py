import math 
import random 

#############
#Class structure representing the vector states 
class State: 
    def __init__(self, x, y, cost):
        self.x = x 
        self.y = y 
        self.cost = cost 
#############

#############
#Function to check if the state exists 
def checkState(s, states): 

    check = False
    for x in states: 
        if s.y == x.y and s.x == x.x: 
            check = True
            print ("State replicated\n\n\n")
            return check 
    
    return (check)

#############
#Function to be Optimized 
def eggHolderFunction(x,y): 

    print ("Cost: " + str((-(y+47)*math.sin(math.sqrt(abs((x/2.0) + (y+47)))) -
        x*math.sin(math.sqrt(abs(x-(y+47)))))))

    return (-(y+47)*math.sin(math.sqrt(abs((x/2.0) + (y+47)))) -
        x*math.sin(math.sqrt(abs(x-(y+47))))) 

#############

#############
#Hill Climibing Optimization
def HillClimbing(x, y, costs, states):

    print ("\nHill Climbing")

    j = 0
    while j < 100:
        j += 1 

        x_not = ((random.uniform(0, 1) - 0.5) + x ) 
        y_not = ((random.uniform(0, 1) - 0.5) + y ) 

        ncost = eggHolderFunction(x_not, y_not)

        if (ncost < costs[len(costs) - 1]):
            costs.append(ncost)

            state = State(x_not, y_not, ncost)
            states.append(state) 

            print ("Better\n") 
            break
        else:
            print ("Worse or the same...")
            continue
        

#############

#############
#Main Function to display some information 
def main():

    cost = 0 
    costs = []  
    states = [] 
    i = 0 

    while i < 100: 
        i += 1 
        print ("\nrun: #" + str(i))

        x_in = random.randint(-10000, 10000)
        print ("Initial X: " + str(x_in))
        y_in = random.randint(-10000, 10000)
        print ("Initial Y: " + str(y_in))

        cost = eggHolderFunction(x_in, y_in)
        state = State(x_in, y_in, cost) 

        check = checkState(state, states)
        
        if not check: 
            costs.append(cost)   
            states.append(state)
            
            HillClimbing(x_in, y_in, costs, states)

        else:
            continue
        
    print ("Costs: ")
    print (costs)
    print ("")

    print ("States ((x,y), cost): ")
    for s in states: 
        print("("+ str(s.x) + ", " + str(s.y) + ")", end = " ") 
        print (s.cost)
#############
    

if __name__ == "__main__":
    main()