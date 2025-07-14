def countPalindrome(text):
    count = 0
    for i in range(1,len(text)):
        #odd len palindromes
        p,q = i-1,i+1
        currlen = 0
        while p >= 0 and q < len(text) and text[p] == text[q]:
            currlen = (q - p) + 1
            p -= 1
            q += 1
        if currlen > 2:
            count += currlen//2

        #even len palindromes
        p,q = i-1,i
        currlen = 0
        while p >= 0 and q < len(text) and text[p] == text[q]:
            currlen = (q - p) + 1
            p -= 1
            q += 1
        if currlen > 1:
            count += currlen/2

    return int(count)


print(countPalindrome("aabbaass"))

