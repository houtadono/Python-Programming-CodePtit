import string

TRANS = string.digits+string.ascii_uppercase

for _ in range(int(input())):
    n, k = map(int,input().split(' '))
    res = ""
    while n > 0:
        res += TRANS[n%k]
        n//=k
    print(res[::-1])

# done        