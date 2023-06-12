
n = int(input())
res = [i for i in range(1,n+2)]
for i in input().split():
    if int(i) in res:
        res.remove(int(i))
print(res[0])

# done