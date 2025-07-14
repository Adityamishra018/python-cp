from copy import deepcopy
import random, time

"""
Lomuto Partition: This is a simple algorithm, we keep track of index of smaller elements and keep swapping. We have used it here in this article because of its simplicity.

Hoare's Partition: This is the fastest of all. Here we traverse array from both sides and keep swapping greater element on left with smaller on right while the array is not partitioned.
"""

def quicksort(arr, l=0,r=None):
    arr = deepcopy(arr)
    if r == None:
        r = len(arr) - 1
    
    def partition(l,r):
        i = l-1
        pivot = arr[r] #taking last element as pivot
        for j in range(l,r+1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i + 1

    def quick(l,r):
        if l>=r:
            return
        
        pi = partition(l,r)
        quick(l, pi-1)
        quick(pi+1, r)
    
    quick(l,r)
    return arr

print(quicksort([1,4,2,5,9,7,8,10]))

start_time = time.perf_counter_ns()
res = quicksort(random.sample(range(1,1_000_000), 20000))
end_time = time.perf_counter_ns()
print(len(res), f' in {(end_time-start_time)/1_000_000:.2f} milliseconds')



