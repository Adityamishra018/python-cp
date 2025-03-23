from collections import deque

tree = [
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def bfs(tree,start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f" {node} ")
            visited.add(node)

            for v,e in enumerate(tree[node]):
                if e == 1 and v not in visited:
                    queue.append(v)
    return visited

bfs(tree,0)