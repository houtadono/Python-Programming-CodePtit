
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
    data = input()
    if data == '0': break
    k, s= data.split(' ')
    k = int(k)
    res = ""
    for i in range(len(s)):
        res += P[ (P.find(s[i])+k) % 28 ]
    print(res[::-1])

# done