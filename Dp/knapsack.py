weights = [2,3,1,5,4,5,2]
values = [100,80,50,60,40,90,30]
knapsize = 12

def KnapSack(weights,values,knapsize):
    dp = [[0 for i in range(knapsize+1)] for _ in range(len(weights)+1)]
    for i in range(1,len(dp)):
        for j in range(knapsize+1):
            if weights[i-1] > j:
                dp [i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],values[i-1] + dp[i-1][j-weights[i-1]])
    #print(dp)            
    return dp[len(weights)][knapsize]

print(KnapSack(weights,values,knapsize)) #320