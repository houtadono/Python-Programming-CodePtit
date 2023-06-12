
from math import inf, sqrt

def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0: return False
    return True

def getUp(n):
    res = 0
    while not prime(n+res): res += 1
    return res

def getDown(n):
    res = 0
    while n-res >= 2 and not prime(n-res): res += 1
    return res if res < n-1 else inf

n = int(input())
a = [int(x) for x in input().split()]
res = 0
for i in a:
    res = max(res,min(getUp(i),getDown(i)))
print(res)

# done