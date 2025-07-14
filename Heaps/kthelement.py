import heapq

def kthsmallest(arr, k):
    heap = []
    for i in arr:
        heapq.heappush(heap, -i)
        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)
    return -1 * heap[0]


def kthlargest(arr, k):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)
    return heap[0]

arr = [2,3,1,4,5,10,11]

print(kthsmallest(arr,3))
print(kthlargest(arr,3))