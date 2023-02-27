
from math import prod

for _ in range(int(input())):
    n = list(map(int,input()))
    r1 = prod(list(filter(lambda i : int(i) > 0 ,n[::2])))
    r2 = sum(n[1::2])
    print(r1, r2)

# done