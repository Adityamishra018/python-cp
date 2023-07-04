def kadane(arr):
    start = end = maxSofar = maxEndingHere = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > arr[i] + maxEndingHere:
            start = i
            maxEndingHere = arr[i]
        else:
            maxEndingHere = arr[i] + maxEndingHere

        if maxEndingHere > maxSofar:
            maxSofar = maxEndingHere
            end = i

    return (maxSofar,start,end)

print(kadane([-2,1,-3,4,-1,2,1,-5,4]))