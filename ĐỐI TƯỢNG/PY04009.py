
class SoPhuc:
    def __init__(self, thuc, ao) -> None:
        self.thuc, self.ao = thuc, ao
        pass

    def __add__(self, p):
        return SoPhuc(self.thuc+p.thuc, self.ao+p.ao)
    
    def __mul__(self, p):
        return SoPhuc(self.thuc*p.thuc - self.ao*p.ao, self.thuc*p.ao+self.ao*p.thuc)
    
    def __pow__(self, o):
        res = self
        while o > 1:
            res = res * self
            o-=1
        return res

    def __str__(self) -> str:
        dau = '+'
        if self.ao < 0: dau = '-'
        return f"{self.thuc} {dau} {abs(self.ao)}i"
    
if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        data = list(map(int,input().split()))
        a = SoPhuc(data[0],data[1])
        b = SoPhuc(data[2],data[3])
        c = (a+b)*a
        d = (a+b)**2
        print(f"{c}, {d}")

# done