
for _ in range(int(input())):
    n, x, m = [float(i) for i in input().split()[:3]]
    res = 0
    while n*pow(x/100+1,res) < m:
        res+=1
    print(res)


# done