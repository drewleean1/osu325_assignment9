#Name: Andrew Lee
#OSU 325
#Assignment 9
#Due date: March 13, 2023

def nonZeroMin(input, visited):
    '''helper function for solve_tsp. this function looks for the next valid min in the neighbors of just one node
    (input). It makes sure that the next valid min is not already visited. Returns a tuple (next valid min, weight)
    to be used by solve_tsp. Similar function used in my assignment 7'''
    minimum_value = (0, float('inf'))                           #tuple (next valid min, weight)
    for x in range(len(input)):                                 #go through all neighbors of input node
        if input[x] != 0 and input[x] < minimum_value[1]:       #check weights
            temp_min = (x, input[x])
            if temp_min[0] not in visited:                      #if not already visited, we have our new min
                minimum_value = temp_min
    return minimum_value

def solve_tsp(G):
    '''function that implements the Nearest Neighbor heurisitc to solve the TSP for a given graph. Assumes that there is
    a possible TSP solution for given G'''
    current_vertex = G[0]
    visited = [0]

    while len(visited) < len(G):
        #while loop that looks for the nearest neighbor of each node
        next_vertex = nonZeroMin(current_vertex, visited)
        visited.append(next_vertex[0])
        current_vertex = G[next_vertex[0]]

    #connect the last node to the starting node
    visited = visited[1:]
    next_vertex = nonZeroMin(current_vertex, visited)
    visited.append(next_vertex[0])
    visited.insert(0, 0)

    return visited