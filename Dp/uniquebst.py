"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n
"""

def uniquebst(n):
    print('called for ', n)
    if n <= 1:
        return 1
    ans = 0
    for i in range(1,n+1):
        ans += uniquebst(i-1) * uniquebst(n-i)
    return ans

print(uniquebst(3))
print(uniquebst(3))
print(uniquebst(4))
