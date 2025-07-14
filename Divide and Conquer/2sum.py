
def binarysearch(arr, target, l=0, r=None):
    if r == None:
        r = len(arr) - 1

    if l>r:
        return -1 

    m = l + (r-l)//2

    if arr[m] == target:
        return arr[m]
    elif arr[m] < target:
        return binarysearch(arr, target, m+1, r)
    elif arr[m] > target:
        return binarysearch(arr, target, l, m-1)
    


def twosum(arr, target):
    arr = sorted(arr)
    pairs = []
    for i,v in enumerate(arr):
        c = binarysearch(arr, target - v, i+1)
        if c != -1:
            pairs.append((v,c))
    print(pairs)

twosum([5, 2, 7, 1, 4],9)


def twosumhash(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return True
        s.add(num)
    return False

arr = [0, -1, 2, -3, 1]
target = -2

if twosumhash(arr, target):
    print("true")
else:
    print("false")