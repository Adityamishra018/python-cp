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