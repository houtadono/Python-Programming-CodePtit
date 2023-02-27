
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    check = 1
    for c in Counter(map(int , input().split())).items():
        if c[1]>n/2:
            check = 0
            print(c[0])
    if check:
        print("NO")

# done