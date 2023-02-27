
k = int(input().split(' ')[1])
s = set(map(int, input().split(' ')))

# n = len(s)
# s = list(s)
# res = [-1]*(k+1)
# def ql(i):
#     if i == k+1:
#         for i in res[1:]:
#             print(s[i],end=' ')
#         print()
#         return
#     for j in range(res[i-1]+1, n-k+i, 1):
#         res[i] = j
#         ql(i+1)
# ql(1)

from itertools import combinations
res = combinations(s,k)
for i in res:
    for j in i:
        print(j,end=' ')
    print()

# done