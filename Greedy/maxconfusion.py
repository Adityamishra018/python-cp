"""
2024. Maximize the Confusion of an Exam
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
"""

#Brute force, will TLE
def maxConfusion(s,k):
    ans = 1
    def longestSub(s):
        nonlocal ans
        sum = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                sum += 1
                ans = max(ans,sum)
            else:
                sum = 1
    def solve(s,k,j):
        if k >=1 :
            for i in range(j,len(s)):
                s[i] = 'T' if s[i] == 'F' else 'F'
                longestSub(s)
                solve(s,k-1,j+1)
                s[i] = 'T' if s[i] == 'F' else 'F'
    longestSub(s)
    solve(list(s),k,0)
    return ans

print(maxConfusion("FTFFT",1))

#sliding window
def maxConsecutiveAnswers(s, k):
    ans = 1
    freq = {'T' : 0,'F' : 0}  #freq of characters in window
    j = 0 #window left idx
    for i in range(len(s)):   #window right idx
        freq[s[i]] += 1
        max_freq_key = 'T' if freq['T'] > freq['F'] else 'F' 
        if freq[max_freq_key] + k >= i-j+1:
            ans = max(ans,i-j+1)
        else:
            freq[s[j]] -= 1
            j += 1
    return ans

print(maxConsecutiveAnswers("TTFTTFTF",2))