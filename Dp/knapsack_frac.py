weights = [10,20,30]
values = [60,100,120]

knapsack = 45

def fracKnapsack(weights,values,knapsack):
    ratio = sorted(zip(values,weights),key = lambda x : x[0]/x[1] , reverse=True)
    ans = 0
    for item in ratio:
        if knapsack >= item[1]:
            ans += item[0]
            knapsack -= item[1]
        else:
            ans += knapsack*(item[0]/item[1])
            break
    return ans

print(fracKnapsack(weights,values,knapsack))