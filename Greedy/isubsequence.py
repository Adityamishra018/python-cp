#two pointer recursion
def isSubSequence(s,t):
    def solve(i,j):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if s[i] == t[j]:
            return solve(i-1,j-1)
        else:
            return solve(i-1,j)
    return solve(len(s)-1,len(t)-1)

print(isSubSequence("avcsvc","vsd"))