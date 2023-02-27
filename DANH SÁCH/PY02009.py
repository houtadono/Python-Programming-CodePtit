
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = []
    while n>0:
        n-=1
        arr.append(int(input()))
    tmp = dict(sorted(Counter(arr).items()))
    a = sorted(tmp.items(), key = lambda i: i[1], reverse= True)
    print(a[0][0])

# done