"""
Given arr A containing maximum number of steps you can take at any A[i], find minimum number of steps to go out of array

"""

def minjumps(arr):
    n = len(arr)
    jumps = 0
    max_reach, curr_reach = 0,0

    for i in range(n):
        max_reach = max(max_reach, i + arr[i])

        if i == curr_reach:
            jumps += 1
            curr_reach = max_reach

        if max_reach >= n:
            return jumps


print(minjumps([2,1,1,2,1]))
print(minjumps([1,1,1,5,1,1]))
print(minjumps([2,3,1,1,1]))