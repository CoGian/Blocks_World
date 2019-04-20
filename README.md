# Blocks_World
This is an assignment for the course of Artificial Intelligence at the University of Macedonia .The goal of the assignment is to make a solver for any [blocks](http://www.cs.colostate.edu/meps/repository/aips2000.html#blocks) configuration .

## Methods implemented : 


  ### Uniformed Search
1) breadth (Breadth-First Search
2) depth (Depth-First Search)

  ### Informed Search
1) best (Best-First Search))
2) astar (A-Star Search)
    ##### Heuristics used: 
    1) Heuristic 1 - this heuristic calculates the number of blocks that are currently not in the correct 'position'.
    
    2) Heuristic 2 - this heuristic is twice the number of blocks that must be moved once plus four times the number of
    blocks that must be moved twice. A block that must be moved once is a block that is currently on a block
    different to the block upon which it rests in the goal state or a block that has such a block somewhere below it
    in the same pile. A block that must be moved twice is a block that is currently on the block upon which it must
    be placed in the goal state, but that block is a block that must be moved or if there exists a block that must be
    moved twice somewhere below it (in the same pile).
    
    3) Heuristic 3 - this heuristic is similar to Heuristic 1. It calculates the difference between the current state
     and the goal state, but looks at the details of each block. If Block A in the goal state is supposed to be on top
     of Block B and under Block C and in the current state it is neither on top of B nor under C, then we add 2 to the
     heuristic and if it is either on top of B or under C we add 1. 
    

## USAGE

###### OS : Windows 10  
###### Version: Python 3.7.1
###### Modules Used: sys, os, re, time, heapq, collections . 
 
##### Type in cmd:  
```bash
python bw.py <method> <problem file> <solution file>
```
Problem files are in directory input_files you can choose from those problems or download [more](http://www.cs.colostate.edu/meps/repository/aips2000.html#blocks).
Moreover you can choose your solution file name or use a standard name like 'solution.txt'. 
##### Output if a solution was found: 
```bash
cost_of_path: the number of moves taken to reach the goal

nodes_expanded: the number of nodes that have been expanded

max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm

running_time: the total running time of the search instance, reported in seconds

valid_solution: true or false depending on the check of solution.
```    

The sequence of moves taken to reach the goal is written in solution file that user have typed above.

##### Example: 
```bash
python bw.py astar probBLOCKS-6-1.pddl solution.txt 
```

```bash
SUCCESS
cost_of_path: 5
nodes_expanded: 16
max_search_depth: 5
running_time: 0.0020017623901367188
valid_solution: true
```

sequence of moves in solution.txt : 
```bash
1. Move(A,F,D)
2. Move(B,table,A)
3. Move(C,table,B)
4. Move(F,table,C)
5. Move(E,table,F)
```

**For more information regarding this project please check my comments inside the code .**
