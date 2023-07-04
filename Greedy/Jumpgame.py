def jumpGame(arr):
    reach = 0
    for i in range(len(arr)):
        if i <= reach:
            reach = max(reach,i + arr[i])
        else:
            return False
    return True

def jumpGame2Dp(arr):
    dp = [float('inf') for _ in range(len(arr))]
    dp[0] = 0
    for i in range(len(arr)):
        for j in range(1,arr[i]+1):
            if j + i < len(arr):
                dp[j+i] = min(dp[j+i],1 + dp[i])
            if dp[-1] != float('inf'):
                return dp[-1]
    return dp[-1]

#return min no of jumps
def jumpGame2Greedy(arr):
    reach = [-1 for _ in range(len(arr))]
    reach[0] = arr[0]
    for i in range(1,len(arr)):
        reach[i] = max(i+arr[i],reach[i-1])   #max index you can reach by directly jumping from i
    
    idx,jump = 0,0
    while idx < len(arr) -1:
        idx = reach[idx]                      # keep jumping max and counting
        jump +=1
    return jump

print(jumpGame([3,2,1,0,4]))
print(jumpGame2Dp([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(jumpGame2Greedy([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
