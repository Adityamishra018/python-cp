def mergearray(arr, left, right):
    sortedarr = []
    i, j= 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedarr.append(left[i])
            i += 1
        elif left[i] > right[j]:
            sortedarr.append(right[j])
            j += 1
    
    while i < len(left):
        sortedarr.append(left[i])
        i += 1
        
    while j < len(right):
        sortedarr.append(right[j])
        j += 1
        
    return sortedarr

def flatten(arr):
    collection = []
    toplevel = []
    for e in arr:
        if not isinstance(e, list):
            toplevel.append(e)
        else:
            collection.append(e)
    collection.append(toplevel)
    flatlist = mergearray(collection, collection[0], collection[1])
    for i in range(2,len(collection)):
        flatlist = mergearray(collection, flatlist, collection[i])
    return flatlist
    

arr = [4,5,6, [12, 13], [1,2], 7, 8]
print(flatten(arr))


    
    
    
        

