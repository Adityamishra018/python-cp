"""
120. Triangle 

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""

#plain recursion
def minPathTriangle(triangle):
    m = len(triangle) - 1
    def solve(i,j):
        if j >= len(triangle[i]):
            return float('inf')
        if i == m:
            return triangle[i][j]
        return min(triangle[i][j] + solve(i+1,j),triangle[i][j] + solve(i+1,j+1))

    return solve(0,0)

#memoized
def minPathTriangleMemo(triangle):
    m = len(triangle) - 1
    memo = {}
    def solve(i,j):
        if j >= len(triangle[i]):
            return float('inf')
        if (i,j) in memo:
            return memo[(i,j)]

        if i == m:
            return triangle[i][j]
        memo[(i,j)] =  min(triangle[i][j] + solve(i+1,j),triangle[i][j] + solve(i+1,j+1))
        return memo[(i,j)]
    return solve(0,0)

#Dp bottom up
def minPathTriangleDp(triangle):
    m = len(triangle)
    dp = [[float('inf') for i in range(m)] for _ in range(m)]
    for i in range(m):
        dp[m-1][i] = triangle[m-1][i]
    for r in range(m-2,-1,-1):
        for c in range(len(triangle[r])):
            dp[r][c] = min(triangle[r][c] + dp[r+1][c],triangle[r][c] + dp[r+1][c+1] )
    return dp[0][0]

print(minPathTriangleMemo([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minPathTriangleDp([[2],[3,4],[6,5,7],[4,1,8,3]]))

