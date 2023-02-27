
class CuaRo:
    def __init__(self, ten, donvi, thoidiem) -> None:
        self.ten = ten
        self.donvi = donvi
        self.ma = ''.join(i[0] for i in donvi.split() + ten.split())
        h, m = map(int, thoidiem.split(':'))
        self.vantoc = 120/(h+m/60-6)
        pass

    def __str__(self) -> str:
        return "{} {} {} {} Km/h".format(self.ma,self.ten,self.donvi,round(self.vantoc))

if __name__ == '__main__':
    arr = [CuaRo(input(),input(),input()) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.vantoc)
    for i in arr:
        print(i)

# done