
from itertools import combinations
from math import gcd
input()
arr = sorted(set(map(int, input().split())))
for i in combinations(arr,2):
    if gcd(i[0],i[1]) == 1:
        print(i[0],i[1])

# done