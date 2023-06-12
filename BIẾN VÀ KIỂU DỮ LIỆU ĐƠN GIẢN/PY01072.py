
a,k = map(int, input().split())
s = list(set(map(int, input().split())))
s.sort()

from itertools import combinations
res = combinations(s,k)
for i in list(res):
    print(*i)

# done