
from math import gcd

class PhanSo:
    def __init__(self, t, m) -> None:
        self.tu = t
        self.mau = m

    def rut_gon(self):
        ucln = gcd(self.tu,self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

if __name__ == '__main__':
    data = list(map(int,input().split()))
    p = PhanSo(data[0],data[1])
    p.rut_gon()
    print(p)

# done