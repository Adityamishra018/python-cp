#you can only buy and sell one stock once
def besttimetobuyandsell(prices):
    if len(prices) < 2:
        return 0
    minPrice,maxProfit =  prices[0],0
    for p in prices:
        maxProfit = max(maxProfit,p - minPrice)
        minPrice = min(minPrice,p)
    return maxProfit

#you can buy and sell one stock any number of times
def besttimetobuyandsell2(prices):
    if len(prices) < 2:
        return 0
    minPrice,profit =  prices[0],0
    for p in prices:
        if p - minPrice > 0:
            profit += p - minPrice
            minPrice = float('inf')
        minPrice = min(minPrice,p)
    return profit

#you can do at most k transaction still can only hold one stock at  a time
def besttimetobuyandsell3(prices,k):
    if len(prices)<2 or k<1:
        return 0
    buy,profit  = [float('-inf')]*k,[0]*k
    for i in range(len(prices)):
        buy[0] = max(buy[0],-prices[i])
        profit[0] = max(profit[0],buy[0] + prices[i])
        for j in range(1,k):
            buy[j] = max(buy[j],profit[j-1] - prices[i])
            profit[j] = max(profit[j],buy[j] + prices[i])
    return profit[-1]

        
print(besttimetobuyandsell([7,1,5,3,6,4]))
print(besttimetobuyandsell2([7,1,5,3,6,4]))
print(besttimetobuyandsell3([7,1,5,3,6,4,8],3))
