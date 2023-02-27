
for _ in range(int(input())):
    input()
    arr = list(map(lambda i: [sum(map(int,i)), int(i)], input().split()))       
    arr.sort()
    for i in arr:
        print(i[1],end=' ')
    print()
    
# done