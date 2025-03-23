"""
Find minimum spanning tree , given a graph
assumed that weights are positive and greater than equal to 1

"""

import heapq

graph = [[0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]]

def prim(graph):
    mset = [0] * len(graph) #keeps track of included nodes
    dist = [(float('inf'),-1)] * len(graph) #keeps distance with parent
    
    #initialize to pick 0th node first
    dist[0] = (0,-1)

    #check if all nodes visited
    while len(list(filter(lambda x : x == 0,mset))) != 0:           
        #find next node to include and add to set
        cost = float('inf');nxt_node = -1
        for i in range(len(dist)):
            if mset[i] == 0 and dist[i][0] < cost:
                cost = dist[i][0]
                nxt_node = i
        mset[nxt_node] = 1  

        #update distance
        for j,v in enumerate(graph[nxt_node]):
            if v != 0 and dist[nxt_node][0] + graph[nxt_node][j] < dist[j][0]:
                dist[j] = (dist[nxt_node][0] + graph[nxt_node][j], nxt_node)
    
    #print edges picked
    for i in range(1,len(dist)):
        print(i, ' ---- ',dist[i][1])

def prim_heap(graph):
    node_heap = []
    mset = [False] * len(graph)
    dist = [float('inf')] * len(graph)
    path = [-1] * len(graph)

    #initialize
    dist[0] = 0
    heapq.heappush(node_heap,(0,0))
    
    while len(list(filter(lambda x : x == 0,mset))) != 0:
        d,i = heapq.heappop(node_heap)
        mset[i] = True 
        for j in range(len(graph[i])):
            if graph[i][j] != 0 and mset[j] == False and d + graph[i][j] < dist[j]:
                dist[j] = d + graph[i][j]
                path[j] = i
                heapq.heappush(node_heap,(dist[j],j))

    for i in range(1,len(path)):
        print(i, ' ---- ',path[i])

prim(graph)
print("------------------------")
prim_heap(graph)