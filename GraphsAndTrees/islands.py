grid = [
    ["0","1","1","0","0"],
    ["0","0","0","1","1"],
    ["0","0","0","1","0"],
    ["0","0","0","0","0"],
]

def is_valid(grid, i,j):
    if i < len(grid) and j < len(grid[i]) and i >= 0 and j >= 0:
        return True
    return False

def bfs(grid, i , j, visited):
    if is_valid(grid,i-1,j):
        if grid[i-1][j] == "1" and not visited[i-1][j]:
            visited[i-1][j] = True
            bfs(grid, i-1, j, visited)
    if is_valid(grid,i+1,j):
        if grid[i+1][j] == "1" and not visited[i+1][j]:
            visited[i+1][j] = True
            bfs(grid, i+1, j, visited)
    if is_valid(grid,i,j-1):
        if grid[i][j-1] == "1" and not visited[i][j-1]:
            visited[i][j-1] = True
            bfs(grid, i, j-1, visited)
    if is_valid(grid,i,j+1):
        if grid[i][j+1] == "1" and not visited[i][j+1]:
            visited[i][j+1] = True
            bfs(grid, i, j+1, visited)


def count_island(grid):
    visited = [[False for j in range(len(grid[i]))] for i in range(len(grid))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and not visited[i][j]:
                count += 1 
                visited[i][j] = True
                bfs(grid,i,j, visited)
    return count

print(count_island(grid))


"""
1. Largest sqaure island

use Dp with this function to update matrix
mat[i,j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1

2. Larget rectange island

use Dp with this function to update matrix
if 1 then mat[i,j] = 1 + mat[i-1][j]
if 0 then mat[i,j] = 0

then apply max_rectangle_hist on each row and take max of them for answer.


"""