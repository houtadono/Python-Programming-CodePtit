
class Matrix:
    def __init__(self, n, m, arr) -> None:
        self.n = n
        self.m = m
        self.arr = arr
    
    def invert(self):
        brr = []
        for i in range(self.m):
            brr.append([self.arr[j][i] for j in range(self.n)])
        return Matrix(self.m,self.n,brr)

    def __mul__(self, p):
        crr = []
        for i in range(self.n):
            tmp = []
            for j in range(self.n):
                tmp.append(sum([self.arr[i][k]*p.arr[k][j] for k in range(self.m)]))
            crr.append(tmp)
        return Matrix(self.n,self.n,crr)
    
    def __str__(self) -> str:
        return "\n".join([ ' '.join([str(self.arr[i][j]) for j in range(self.m) ]) for i in range(self.n) ])

if __name__ == '__main__':
    t = int(input())
    while t>0:
        n, m = map(int, input().split())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        a = Matrix(n,m,arr)
        b = a.invert()
        c = a*b
        print(c)
        t-=1
        
# done