arr = [2,4,1,5,7,3,8,12,0,-3,24]

def lomutoPartition(arr,l=0,h=None):
    if h is None:
        h = len(arr)-1
    p = arr[h]
    i = l-1
    for j in range(l,h-1):
        if(arr[j] > p):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = p,arr[i+1]
    return i+1


print(lomutoPartition(arr),arr)

def haorePartition(arr,l=0,h=None):
    if h is None:
        h = len(arr)-1
    p = arr[l]
    i = l
    j = h
    while True:
        while i< len(arr) and arr[i]<=p:
            i += 1
        while j>= 0 and arr[j] >=p:
            j -= 1

        if i > j:
            return j
        else:
            arr[i],arr[j] = arr[j],arr[i]

print(haorePartition(arr))

def quickSort(arr,l=0,h=None):
    if h is None:
        h = len(arr)-1

    if l < h:
        pidx = haorePartition(arr,l,h)
        arr[l],arr[pidx] = arr[pidx],arr[l]
        quickSort(arr,l,pidx-1)
        quickSort(arr,pidx+1,h)

quickSort(arr)
print(arr)

