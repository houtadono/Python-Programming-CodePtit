
from math import prod

for _ in range(int(input())):
    n = list(map(int,input()))
    r1 = sum(n[::2])
    n2 = list(filter(lambda i : int(i) > 0 ,n[1::2]))
    if len(n2) == 0:
        r2 = 0
    else:
        r2 = prod(n2)
    print(r1, r2)

# done