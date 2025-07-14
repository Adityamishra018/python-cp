def all_visited(visited):
    for r in visited:
        for e in r:
            if not e:
                return False
    return True 

def spiral_print(arr):
    m = len(arr)
    n = len(arr[0])
    visited = [[False for _ in row ] for row in arr]

    rdir = [0,1,0,-1]
    cdir = [1,0,-1,0]

    currdir = 0 #right
    r,c = 0,-1
    while not all_visited(visited):
        if r + rdir[currdir] < m and c + cdir[currdir] < n and not visited[r + rdir[currdir]][c + cdir[currdir]]:
            print(arr[r + rdir[currdir]][c + cdir[currdir]])
            visited[r + rdir[currdir]][c + cdir[currdir]] = True
            r = r + rdir[currdir]
            c = c + cdir[currdir]
        else:
            #change direction
            currdir = (currdir + 1 ) % 4

arr = [
    [1,2,3,4,17],
    [5,6,7,8,18],
    [9,10,11,12,19],
    [13,14,15,16,20]
]

print(spiral_print(arr))
