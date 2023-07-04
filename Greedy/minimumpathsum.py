"""

The minimum path sum problem requires us to write a function called minPathSum() that accepts a 2D list called grid.
Our job is to find a path from the top-left to bottom-right corner of the grid, 
such that the sum of all numbers along the path is the smallest
"""
import copy

def minPathSum(grid):
    cost = copy.deepcopy(grid)
    #update min cost for first row
    for j in range(1,len(grid[0])):
        cost[0][j] = cost[0][j-1] + grid[0][j]
    
    #update for rest of the rows, min could be coming from left or from up
    for i in range(1,len(grid)):
        for j in range(len(grid[i])):
            if j - 1 >= 0:
                cost[i][j] = min(cost[i][j-1] + grid[i][j],cost[i-1][j] + grid[i][j])
            else:
                cost[i][j] = cost[i-1][j] + grid[i][j]
    return cost[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))

        
