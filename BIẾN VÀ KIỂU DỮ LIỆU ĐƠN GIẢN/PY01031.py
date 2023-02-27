import string

TRANS = string.digits+string.ascii_uppercase

for _ in range(int(input())):
    n, b = map(int,input().split(' '))
    res = ""
    while n > 0:
        res += TRANS[n%b]
        n//=b
    print(res[::-1])

# done        