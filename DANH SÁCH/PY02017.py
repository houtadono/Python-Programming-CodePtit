from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for key, value in Counter(arr).items():
        if value&1==1:
            print(key)
            break

# done