
while 1:
    x = list(map(int, input().split()))
    if len(set(x)) == 1 and x[0] == 0: break
    res = 0
    while len(set(x)) != 1:
        res+=1
        tmp = x[0]
        for i in range(3):
            x[i] = abs(x[i]-x[i+1])
        x[-1] = abs(x[-1]-tmp)
    print(res)

# done