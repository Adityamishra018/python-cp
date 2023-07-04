"""
The following mapping is given
'A' -> 1
'B' -> 2
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""

#plain recursion
def decodeWays(s):
    n = len(s)
    def solve(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        res = solve(i+1)
        if i+1<n-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
            res += solve(i+2)
        return res
    return solve(0)

#dp
def decodeWaysDp(s):
    dp = [0 for i in s+"_"]
    dp[len(s)],dp[len(s)-1]  = 1, 1 if s[-1] != '0' else 0
    for i in range(len(s)-2,-1,-1):
        if s[i] == '0':
            continue
        dp[i] = dp[i+1]
        if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
            dp[i] += dp[i+2]
    return dp[0]

print(decodeWays("21103"))
print(decodeWaysDp("20103"))
print(decodeWaysDp("1220221110121201210211212121010201021"))

