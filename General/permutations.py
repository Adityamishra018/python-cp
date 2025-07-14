def generateAllPermutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    perms = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in generateAllPermutations(rest):
            perms.append(p + [arr[i]])
    return perms

print(generateAllPermutations(list("abc")))
