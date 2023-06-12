
from itertools import combinations
from math import gcd
n = int(input())
arr = sorted(set(map(int, input().split())))[:n]
for i in combinations(arr,2):
    if gcd(i[0],i[1]) == 1:
        print(i[0],i[1])

# done