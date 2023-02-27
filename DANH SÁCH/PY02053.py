
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())

s1 = sum( [ sum(arr[i][:n-i-1]) for i in range(n-1) ])
s2 = sum( [ sum(arr[i][n-i:])   for i in range(1,n) ])
res = abs(s1-s2)

print("YES") if res <= k else print("NO")
print(res)

# done