
for _ in range(int(input())):
    n, m = map(int, input().split())
    x = [list(map(int, input().split())) for i in range(n)]
    h = [list(map(int, input().split())) for i in range(3)]
    
    def convolution():
        u = n - 2
        v = m -2
        res = 0
        for i in range(u):
            for j in range(v):
                res += sum([sum([x[i1+i][i2+j]*h[i1][i2] for i2 in range(3)]) for i1 in range(3)])
        return res           
    print(convolution())

# done