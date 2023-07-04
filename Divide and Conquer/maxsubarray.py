def crosssubarray(arr,l,p,r):
    left_sum = right_sum = arr[p]
    sum = arr[p]
    i = p-1
    while i >= l:
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
        i -=1
    sum = arr[p]
    i=p+1
    while i <= r:
        sum = sum + arr[i]
        if sum > right_sum:
            right_sum = sum
        i +=1
    return max(left_sum+right_sum-arr[p],left_sum,right_sum)

def maxsubarray(arr,l,r):
    if l>r:
        return float('-inf')
    if l==r:
        return arr[l]
        
    p = (l+r)//2
    
    lss = maxsubarray(arr,l,p-1)
    rss = maxsubarray(arr,p+1,r)
    css = crosssubarray(arr,l,p,r)
    return max(lss,rss,css)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarray(arr,0,len(arr)-1))