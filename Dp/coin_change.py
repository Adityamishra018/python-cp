"""
Given different denominations and an integer amount, assuming you have infinte coins, find minimum no of coins required

variation 1 = total no of ways (remove the min check and just add all ways)
variation 2 = limited no of coins 

"""

#recursion
def coinChange(arr,m):
    if m == 0:
        return 0

    min_count = float('inf')
    for c in arr:
        if c<=m:
            min_count = min(min_count,1 + coinChange(arr,m-c))
    return min_count

#memoization
def coinChangeMemo(arr,m):
    memo = {}
    def solve(m):
        if m == 0:
            return 0

        min_count = float('inf')
        for c in arr:
            if c<=m:
                min_count = min(min_count,1 + solve(m-c))
        memo[m] = min_count
        return memo[m]
    
    return solve(m)

def coinChangeDp(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float('inf') else -1

arr = [1,2,5]
amount = 100

#print(coinChange(arr,amount))
#print(coinChangeMemo(arr,amount))
print(coinChangeDp(arr,amount))