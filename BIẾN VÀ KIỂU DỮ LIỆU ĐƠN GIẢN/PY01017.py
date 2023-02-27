
for _ in range(int(input())):
    s = input()
    res = ""
    i = 0

    while i < (len(s)):
        c = s[i]
        d = 0
        while i < len(s) and c == s[i] : 
            d+=1
            i+=1
        res = res + str(d)+c
    print(res)

# done