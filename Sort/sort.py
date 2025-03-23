from copy import deepcopy
import random, time

def bubblesort(arr):
    arr = deepcopy(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selectionsort(arr):
    arr = deepcopy(arr)
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def insertionsort(arr):
    arr = deepcopy(arr)
    for i in range(1,len(arr)):
        key, j = arr[i], i-1
        while j >=0:
            if arr[j] > key:
                arr[j+1] = arr[j]   
            else:
                break
            j -= 1
        arr[j+1] = key
    return arr

arr = [1,4,21,3,10,7,5]
print(bubblesort(arr))

start_time = time.perf_counter_ns()
res = bubblesort(random.sample(range(1,1_000_000), 20000))
end_time = time.perf_counter_ns()
print(len(res), f' in {(end_time-start_time)/1_000_000:.2f} milliseconds')






