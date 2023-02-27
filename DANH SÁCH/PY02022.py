
from collections import Counter
from math import sqrt

def ngto(n):
    if n==2: return True
    if n<2 or n % 2 == 0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

input()
arr = map(int, input().split())
for i in Counter(arr).items():
    if ngto(i[0]):
        print(i[0],i[1])

# done