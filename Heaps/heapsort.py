from copy import deepcopy
import time, random

class MinHeap:
    def __init__(self, arr=[]):
        self.heap = arr
        self.createheap()

    def push(self, key):
        self.heap.append(key)
        idx = len(self.heap) -1 
        while idx > 0 and self.heap[(idx - 1//2) - 1] > self.heap[idx]:
            self.heap[idx], self.heap[(idx - 1//2) - 1] = self.heap[(idx - 1//2) - 1], self.heap[idx]
            idx = (idx - 1//2) - 1

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return max_val

    def __str__(self):
        str_arr = [str(x) for x in self.heap]
        return " ".join(str_arr)
    
    def heapify(self, idx):
        smallest = idx
        left = idx*2 + 1
        right = idx*2 + 2

        if idx < len(self.heap):
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if idx != smallest:
                self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
                self.heapify(smallest)

    def createheap(self):
        idx = len(self.heap)//2 - 1
        for i in range(idx,-1,-1):
            self.heapify(i)


def heapsort(arr):
    heap = MinHeap(arr)
    arr = []
    while True:
        ele = heap.pop()
        if ele is not None:
            arr.append(ele)
        else:
            break
    return arr


print(heapsort([1,4,5,2,7,3,9]))

start_time = time.perf_counter_ns()
res = heapsort(random.sample(range(1,1_000_000), 20000))
end_time = time.perf_counter_ns()
print(len(res), f'in {(end_time-start_time)/1_000_000:.2f} milliseconds')


