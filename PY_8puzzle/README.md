# Python Implementation of the 8 Puzzle Problem

### Compile and execute source code 

* Install Anaconda3
* Open command prompt 
* Create a conda environment 
* Activate the enviornment 
```
conda create --name *env_name*
conda activate *env_name*
```

* Install necessary package(s) 
```
conda install numpy
```

* Create a text file containing the array to find the solution to 
	* Enter matrix entries one by one (1 2 3 4 ... )
		* Seperate with space 
		* Leave no space on the end or at the beginning 
	* Name something simple such as "state.txt"
	
* Run the code 
```
python 8puzzle.py
```

* Enter the text file containing the desired array 
	* Simply ("state.txt")
		* When on the command line, neglect use of quotes 

* Choose the type of search desired 
	* 1 for Breadth-First 
	* 2 for Depth-First 

* Wait for the program to find the solution

## Example: 

![Example Matrix](https://github.com/njenn001/cs480/blob/master/PY_8puzzle/sample.JPG)

### Using Breadth-First Search 

![BFS Solution](https://github.com/njenn001/cs480/blob/master/PY_8puzzle/sampleBreadth.JPG)
* Path: 
	* 3 moves to find solution 
* Compilation Time:
	* About 1 millisecond 	

### Using Depth-First Search
![DFS Solution](https://github.com/njenn001/cs480/blob/master/PY_8puzzle/sampleDepth.JPG)
* Path: 
	* 3 moves to find solution 
* Compilation Time: 
	* About 5 miliseconds 

### Comparison 
The two search algorithms could find the goal successfully. This example shows the paths to the goal were the same; however, this is not true for ever initial state. The example also shows that the time to execute the Breadth-First search is about one fifth of the time it took to execute the Depth-First search. 


