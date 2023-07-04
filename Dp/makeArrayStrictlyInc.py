"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

https://leetcode.com/problems/make-array-strictly-increasing/solutions/3647976/c-a-true-o-m-n-time-solution-that-s-very-easy-too/
"""
import bisect

#At every index we have two options proceed with same value, proceed with smallest swappable element from array2
def makeArrayIncreasingDp(arr1, arr2):
        arr2.sort()
        memo = {}
        def findNext(i,past=-1):
            if i == len(arr1):
                return 0
            if (i, past) in memo:
                return memo[(i, past)]

            count = float('inf')
            
            if arr1[i] > past:
                count = findNext(i+1,arr1[i]) #not take
            
            swapIdx = bisect.bisect_right(arr2,past)
            if swapIdx < len(arr2):
                count = min(count,1+findNext(i+1,arr2[swapIdx])) #take
                
            memo[(i, past)] = count
            return count
            
        ans = findNext(0)
        return ans if ans != float('inf') else -1 

print(makeArrayIncreasingDp([1,5,3,6,7],[4,3,1]))