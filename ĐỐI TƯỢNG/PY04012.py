
class SinhVien:
    def __init__(self, ma, ten, lop) -> None:
        self.ma, self.ten, self.lop = ma, ten, lop
        pass

    def setDcc(self, s):
        self.dcc = 10 - str(s).count('v')*2 - str(s).count('m')
        self.gc = ''
        if self.dcc <= 0 : 
            self.dcc = 0
            self.gc = 'KDDK'

    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.ma, self.ten, self.lop, self.dcc, self.gc)
    
if __name__ == '__main__':
    t = int(input())
    ds = []
    for _ in range(t):
        ds.append(SinhVien(input(),input(),input()))
    
    for _ in range(t):
        ma, s = input().split()
        for i in ds:
            if i.ma == ma:
                i.setDcc(s)
    
    for i in ds:
        print(i)

# done