#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Name : SHRIYA REDDY PULAGAM, Usename : spulagam
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

#Returns if new house map is acceptable or not    
def is_acceptable_housemap(new_house_map):
    w=[]
    w.append(check_row(new_house_map))#calls check_row
    w.append(check_col(new_house_map))#calls check_col
    w.append(check_left_diag(new_house_map))#check_left_diag
    w.append(check_right_diag(new_house_map))#check_right_diag
    if all(w):
        return True
    else:
        return False


# Checks if p's in all rows in house map are in correct position
def check_row(new_house_map):
    w = []
    p_pos= [] #list containing position of 'p'
    x_pos = [] #list containing position of X and @
    for row in new_house_map:
        for j in range(0,len(row)):
            if row[j] in "X@":
                x_pos.append(j)
            if row[j] == 'p':
                p_pos.append(j)

        for l in p_pos:
            for i in range(l+1,len(row)):#if 'p' finds 'p' next, then it retuns False
                if row[i] == 'p':
                    return False
                elif row[i] in "X@": #else if 'p' finds X or @ next then it breaks out of loop
                    w.append(True)
                    break
        x_pos = []
        p_pos = []
    if all(w):
        return True

            




#checks if p's in all columns in house map are in correct position
def check_col(new_house_map):
    w = []
    p_pos = []
    x_pos = []
    
    for i in range(len(new_house_map[0])):
        collist = []
        for j in range(len(new_house_map)):
            collist.append(new_house_map[j][i])

        for m in range(0,len(collist)):
            if collist[m] in "X@":
                x_pos.append(j)
            if collist[m] == 'p':
                p_pos.append(m)

        for l in p_pos:
            for i in range(l+1,len(collist)):
                if collist[i] == 'p':
                    return False
                elif collist[i] in "X@":
                    w.append(True)
                    break
        x_pos = []
        p_pos = []
    if all(w):
        return True
#checks if p's in all left diagonals in house map are in correct position
def check_left_diag(new_house_map):

    w = []
    
    maxrow = len(new_house_map)
    maxcol = len(new_house_map[0])
    #######The following lines of code are referred from https://izziswift.com/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python/ ######
    min_leftdiag = -maxrow + 1
    rightdiag = [[] for _ in range(maxrow + maxcol - 1)]
    leftdiag = [[] for _ in range(len(rightdiag))]  
    for x in range(maxcol):
        for y in range(maxrow):
            leftdiag[x-y-min_leftdiag].append(new_house_map[y][x])
            
    ################################################################################################################################################

    for k in leftdiag:
        p_pos = []
        x_pos = []
        for m in range(0,len(k)):
            if k[m] in "X@":
                x_pos.append(m)
            if k[m] == 'p':
                p_pos.append(m)

        for l in p_pos:
            for i in range(l+1, len(k)):
                if k[i] == 'p':
                    return False
                elif k[i] in "X@":
                    w.append(True)
                    break
        x_pos = []
        p_pos = []
    if all(w):
        return True
                
#checks if p's in all right diagonals in house map are in correct position    
def check_right_diag(new_house_map):
    w = []
    maxrow = len(new_house_map)
    maxcol = len(new_house_map[0])
    #######The following lines of code are referred from https://izziswift.com/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python/ ######
    rightdiag = [[] for _ in range(maxrow + maxcol - 1)]
    for x in range(maxcol):
        for y in range(maxrow):
            rightdiag[x+y].append(new_house_map[y][x])
    ################################################################################################################################################
    for k in rightdiag:
        p_pos = []
        x_pos = []
        for m in range(0,len(k)):
            if k[m] in "X@":
                x_pos.append(m)
            if k[m] == 'p':
                p_pos.append(m)

        for l in p_pos:
            for i in range(l+1, len(k)):
                if k[i] == 'p':
                    return False
                elif k[i] in "X@":
                    w.append(True)
                    break
        x_pos = []
        p_pos = []
    if all(w):
        return True
    
    
    
           
    
# check if house_map is a goal state
def is_goal(house_map, k):
    if is_acceptable_housemap(house_map):
        return count_pichus(house_map) == k #if number of p's match k and it is an acceptable house map
    else:
        return False
    

 
# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [] 
    fringe.append(initial_house_map)
    while fringe:
        for new_house_map in successors(fringe.pop()):
            if is_goal(new_house_map,k):
                return (new_house_map,True)
            else:
                if is_acceptable_housemap(new_house_map):#if it is not a goal state, then it checks if it is an acceptable house map, if yes it gets appended to fringe
                    fringe.append(new_house_map)
    return(new_house_map, False)

#Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")

    print (printable_house_map(solution[0]) if solution[1] else "False")
