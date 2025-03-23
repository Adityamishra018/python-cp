from copy import deepcopy
import random
import time

def mergesort(arr, l = 0, r = None):
    arr = deepcopy(arr)
    if(r == None):
        r = len(arr) - 1

    def merge(arr, l, m, r):
        arr1 = deepcopy(arr[l:m+1])
        arr2 = deepcopy(arr[m+1:r+1])
        p,q = 0,0
        while p < len(arr1) and q < len(arr2):
            if arr1[p] < arr2[q]:
                arr[l] = arr1[p]
                p += 1
                l += 1
            else:
                arr[l] = arr2[q]
                q += 1
                l += 1

        while p < len(arr1):
            arr[l] = arr1[p]
            p += 1
            l += 1
        
        while q < len(arr2):
            arr[l] = arr2[q]
            q += 1
            l += 1

    def solve(arr, l, r):
        if l >= r:
            return 
        m = l + (r-l)//2

        solve(arr,l,m)
        solve(arr,m+1,r)
        merge(arr, l, m ,r)

    solve(arr, l, r)
    return arr

arr = random.sample(range(1,20000), 10000)
start_time = time.perf_counter_ns()
res = mergesort(arr)
end_time = time.perf_counter_ns()
print(len(res), f' in {(end_time-start_time)/1_000_000:.2f} milliseconds')