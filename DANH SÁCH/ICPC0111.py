
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in arr[k: ]:
        print(i,end=' ')
    for i in arr[:k]:
        print(i,end=' ')
    print()
    
# done