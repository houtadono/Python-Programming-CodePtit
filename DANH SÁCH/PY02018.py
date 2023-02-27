
n = int(input())
res = [i for i in range(1,n+2)]
for i in input().split():
    res.remove(int(i))
print(res[0])

# done