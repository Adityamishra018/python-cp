"""
A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is greater than or equal to its own value. Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.
"""

class MaxHeap:
    def __init__(self, arr=[]):
        self.heap = arr
        self.createheap()

    def push(self, key):
        self.heap.append(key)
        idx = len(self.heap) -1 
        while idx > 0 and self.heap[(idx - 1//2) - 1] < self.heap[idx]:
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
        largest = idx
        left = idx*2 + 1
        right = idx*2 + 2

        if idx < len(self.heap):
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if idx != largest:
                self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
                self.heapify(largest)

    def createheap(self):
        idx = len(self.heap)//2 - 1
        for i in range(idx,-1,-1):
            self.heapify(i)


heap = MaxHeap([14,24,12,11,25,8,35])
print(heap)

heap.push(99)
print(heap)

print(heap.pop())

print(heap)

def heapsort(arr):
    heap = MaxHeap(arr)
    arr = []
    while True:
        ele = heap.pop()
        if ele is not None:
            arr.append(ele)
        else:
            break
    return [i for i in reversed(arr)]

print(heapsort([1,4,5,2,7,3,9]))



