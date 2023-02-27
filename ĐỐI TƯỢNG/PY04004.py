
from math import gcd

class PhanSo:
    def __init__(self, t, m) -> None:
        self.tu = t
        self.mau = m

    def rut_gon(self):
        ucln = gcd(self.tu,self.mau)
        self.tu //= ucln
        self.mau //= ucln

    @staticmethod
    def sum(p, q):
        tu = p.tu*q.mau + q.tu*p.mau
        mau = p.mau * q.mau
        return PhanSo(tu, mau)

    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

if __name__ == '__main__':
    data = list(map(int,input().split()))
    p = PhanSo(data[0],data[1])
    q = PhanSo(data[2],data[3])
    res = PhanSo.sum(p,q)
    res.rut_gon()
    print(res)

# done