
n = int(input())
arr = list(map(int, input().split()))
res = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            res+=1
print(res)

# done