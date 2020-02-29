import math 
import random 

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np 

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

    #print ("Cost: " + str((-(y+47)*math.sin(math.sqrt(abs((x/2.0) + (y+47)))) -
    #    x*math.sin(math.sqrt(abs(x-(y+47)))))))

    return (-(y+47)*math.sin(math.sqrt(abs((x/2.0) + (y+47)))) -
        x*math.sin(math.sqrt(abs(x-(y+47))))) 

#############

#############
#Function to find the smallest value of all generated states 
def findLowest(states, costs, xValues, yValues):

    loop = 0
    low = 0 
    x = 0 
    y = 0 
    for s in states: 
        loop += 1

        #print("("+ str(s.x) + ", " + str(s.y) + ")", end = " ") 
        costs.append(s.cost) 
        xValues.append(s.x)
        yValues.append(s.y) 

        if (loop == 1):
            #print ("Beginning") 
            low = states[0].cost
            x = states[0].x
            y = states[0].y 
        else: 
            if (states[loop - 1].cost < low): 
                low = states[loop - 1].cost
                x = states[loop - 1].x
                y = states[loop - 1].y

                #print ("New lowest cost: " + str(low))

    print ("Minimized Function State: \n")
    print ("X: " + str(x))
    print ("Y: " + str(y))
    print ("Cost: " + str (low))
#############

#############
#Function to implement Differential Evolution
def dEvolution(x, y, costs, states):
    print ("Evolution")

    #print ("\nHill Climbing")

    cCost = 0 

    j = 0
    while True:

        x_not = ((random.uniform(0, 1) - 0.5) + x ) 
        y_not = ((random.uniform(0, 1) - 0.5) + y ) 

        ncost = eggHolderFunction(x_not, y_not)

#############

#############
#Hill Climibing Optimization
def HillClimbing(x, y, costs, states):

    #print ("\nHill Climbing")

    cCost = 0 

    j = 0
    while True:

        x_not = ((random.uniform(0, 1) - 0.5) + x ) 
        y_not = ((random.uniform(0, 1) - 0.5) + y ) 

        ncost = eggHolderFunction(x_not, y_not)

        if (len(costs) > 0):
            if (ncost < costs[len(costs) - 1]):
                j = 0

                x = x_not 
                y = y_not

                costs[len(costs) - 1] = ncost 

                #print ("Better\n") 
                continue
            elif (ncost == costs[len(costs) - 1]):
                j = 0
                costs.append(ncost)

                state = State(x_not, y_not, ncost)
                states.append(state)

                #print ("Similar Cost")
                break
            else:
                #print ("Worse")
                j += 1
                
                if (j > 100): 
                    j = 0
                    costs.append(ncost)

                    state = State(x_not, y_not, ncost)
                    states.append(state)

                    #print ("Finishing...")

                    break
                else:
                    continue
        

#############

#############
#Main Function to display some information 
def main(): 

    print ("\nChoose a search pattern:")
    print ("\n1) Hill Climbing \n2) Differential Evolution ")

    while True:
        try:
            choice = int (input("Choice: "))
        except Exception as ex: 
            print ("Not the correct input type")
            continue
    
        if (choice == 1): 

            cost = 0 
            costs = []  
            states = [] 

            i = 0
            while i < 100: 
                i += 1 

                x_in = random.randint(-10000, 10000)
                y_in = random.randint(-10000, 10000)

                cost = eggHolderFunction(x_in, y_in)
                state = State(x_in, y_in, cost) 
                
                costs.append(cost)   
                states.append(state)
                
                HillClimbing(x_in, y_in, costs, states)

            costs = [] 
            xValues = [] 
            yValues = [] 
            
            findLowest(states, costs, xValues, yValues)
                
                
            fig = plt.figure() 

            ax = plt.axes(projection='3d')
            ax.scatter(xValues, yValues, costs, c = costs, cmap='viridis', linewidth=0.5)
            
            ax.set_title('Minima Distribution')
            ax.plot_trisurf(xValues, yValues, costs, cmap='viridis', edgecolor='none')
            ax.set_xlabel('$X values$', fontsize=10)
            ax.set_ylabel('$Y values$', fontsize=10)
            ax.set_zlabel('$EH(x,y)$', fontsize=10)
            ax.zaxis.set_rotate_label(False) 

            ax.yaxis._axinfo['label']['space_factor'] = 50.0

            plt.show()

            break
        if (choice == 2): 
            cost = 0 
            costs = []  
            states = [] 

            i = 0
            while i < 100: 
                i += 1 

                #print ("\nrun: #" + str(i))

                x_in = random.randint(-10000, 10000)
                #print ("Initial X: " + str(x_in))
                y_in = random.randint(-10000, 10000)
                #print ("Initial Y: " + str(y_in))

                cost = eggHolderFunction(x_in, y_in)
                state = State(x_in, y_in, cost) 

                #check = checkState(state, states)
                
                costs.append(cost)   
                states.append(state)

                dEvolution(x_in, y_in, costs, states) 


            break

    print ("Finished") 

#############
    

if __name__ == "__main__":
    main()