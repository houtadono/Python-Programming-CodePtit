import string

TRANS = string.digits+string.ascii_uppercase

for _ in range(int(input())):
    k = int(input())
    n = int(input(), 2)
    res = ""
    while n > 0:
        res += TRANS[n%k]
        n//=k
    print(res[::-1])

# done        