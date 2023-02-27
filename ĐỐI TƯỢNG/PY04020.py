
class HoaDon:
    def __init__(self, ma, ten, sl, dongia, chietkhau):
        self.ma, self.ten, self.sl = ma, ten,sl 
        self.dongia, self.chietkhau = dongia, chietkhau
        self.tongtien = dongia * sl -chietkhau
        
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.sl, self.dongia, self.chietkhau, self.tongtien)
    

if __name__ == "__main__":
    arr = [HoaDon(input(), input(), int(input()), int(input()), int(input())) for _ in range(int(input()))]
    arr.sort(key = lambda x : -x.tongtien)
    for i in arr:
        print(i)

# done