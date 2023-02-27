
input()
arr = map(int, input().split())

res = {}
for i in arr:
    res[i] = sum(map(lambda j: abs(j-i),arr))

res = sorted(res.items(), key= lambda i: i[1])
print(res[0][1],res[0][0])

# done