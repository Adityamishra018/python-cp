tree = [
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def dfs(tree,start,visited=None):
    if visited == None:
        visited = set()
    visited.add(start)
    print(f" {start} ")
    
    for v,e in enumerate(tree[start]):
        if e == 1 and v not in visited:
            dfs(tree,v,visited)

def dfs_iterative(tree,start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(f" {node} ")
            visited.add(node)
        
            for i in reversed(range(len(tree[node]))):
                if tree[node][i] == 1 and i not in visited:
                    stack.append(i)
            
dfs(tree,0)
dfs_iterative(tree,0)
    
    

