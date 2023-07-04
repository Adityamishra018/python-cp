"""
It takes n steps to reach the top of stairs. You can take 1 or 2 steps at a time.
find total number of ways.

Its fib series
-1 1 0 1 2 3 5 8 13

"""

#plain recurion
def climbingstairs(n):
    if n <= 1:
        return 1
    return climbingstairs(n-1) + climbingstairs(n-2)

#memoize
def climbingstairsMemo(n,memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climbingstairs(n-1) + climbingstairs(n-2)
    return memo[n]

#bottom up is basically fib solution

print(climbingstairsMemo(12,memo={}))

"""
Variation 1

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

"""

#memoize
def climbingstairsCostMemo(costs):
    memo={}
    n = len(costs)
    def solve(idx):
        if idx in memo:
            return memo[idx]

        if idx >= n:
            return 0
        elif idx == n-1:
            return costs[n-1]
        elif idx == n-2:
            return costs[n-2]
        
        memo[n] = min(costs[idx] + solve(idx+2),costs[idx] + solve(idx+1))
        return memo[n]
    return min(solve(0),solve(1))

print(climbingstairsCostMemo([1,100,1,1,1,100,1,1,100,1]))



