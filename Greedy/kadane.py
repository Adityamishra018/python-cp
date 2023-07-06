"""
largest sum subarray
"""

def kadane(arr):
    start = end = maxSofar = maxEndingHere = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > arr[i] + maxEndingHere:
            start = i
            maxEndingHere = arr[i]
        else:
            maxEndingHere = arr[i] + maxEndingHere

        if maxEndingHere > maxSofar:
            maxSofar = maxEndingHere
            end = i

    return (maxSofar,start,end)

print(kadane([-2,1,-3,4,-1,2,1,-5,4]))


"""
Min length subarray
"""
def minSubArrayLen(tar, arr):
    startidx = 0
    ans = float('inf')
    sum = 0
    for i in range(len(arr)):
        if arr[i] + sum == tar:
            ans = min(i - startidx + 1,ans)
            sum += arr[i]
            sum -= arr[startidx]
            startidx += 1
        elif arr[i] + sum < tar:
            sum += arr[i]
        else:
            while(sum + arr[i] > tar):
                sum -= arr[startidx]
                startidx += 1
            if sum + arr[i] == tar:
                ans = min(i - startidx + 1,ans)
                sum -= arr[startidx]
                startidx += 1
            sum += arr[i]
    return ans if ans != float('inf') else 0

print(minSubArrayLen(12,[1,2,3,4,5]))
print(minSubArrayLen(6,[1,2,3,3,4]))

"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

"""

def longestSubarray(nums):
    if getIndex(nums,0) == -1:
        return len(nums)-1
    
    zerocount = ans = res = zeroidx =  0
    for i in range(len(nums)):
        if nums[i] == 0 and zerocount == 0:
            zerocount = 1
            zeroidx = i
            res += nums[i]
            ans = max(res,ans)
        elif nums[i] == 0 and zerocount == 1:
            res = i - zeroidx - 1
            zeroidx = i
            zerocount = 1
            ans = max(res,ans)
        else:
            res += nums[i]
            ans = max(res,ans)
    return ans

def getIndex(nums,v):
    try:
        index_value = nums.index(v)
        return index_value
    except ValueError:
        index_value = -1
        return index_value

print(longestSubarray([0,1,1,1,0,1,1,0,1]))