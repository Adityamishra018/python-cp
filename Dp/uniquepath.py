"""
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

#memoized reursion
def uniquePathCount(m,n):
    m,n = m-1,n-1
    memo = {}
    def solve(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        elif i>m or j>n:
            return 0
        elif i == m and j == n:
            return 1

        memo[(i,j)] = solve(i,j+1) + solve(i+1,j)
        return memo[(i,j)]

    return solve(0,0)

"""
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
imagine the obsgrid as the map. where 1 in map is obstacle

"""

#memoized reursion
def uniquePathWithObstacleCount(obsgrid):
    if obsgrid[0][0] != 0:
        return 0
    m,n = len(obsgrid)-1,len(obsgrid[0])-1
    memo = {}

    def solve(i,j):
        if (i,j) in memo:
            return memo[(i,j)]

        elif i>m or j>n:
            return 0
        elif i == m and j == n:
            return 1

        a = b = 0
        if j + 1 <= n and obsgrid[i][j+1] == 0:
            a = solve(i,j+1)

        if i + 1 <= m and obsgrid[i+1][j] == 0:
            b = solve(i+1,j)

        memo[(i,j)] = a + b
        return memo[(i,j)]

    return solve(0,0)

print(uniquePathCount(20,20))
print(uniquePathWithObstacleCount([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathWithObstacleCount([[0,1],[0,0]]))