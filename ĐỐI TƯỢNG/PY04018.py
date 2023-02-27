
stt = 1
class GiaoVien:
    def __init__(self, ten, ma, d1, d2) -> None:
        global stt
        self.ma = "GV%02d" %(stt)
        stt+=1
        self.ten = ten
        if ma[0] == 'A':
            self.monhoc = "TOAN"
        elif ma[0] == 'B':
            self.monhoc = "LY"
        else:
            self.monhoc = "HOA"
        self.diemUT = 2.0 - (int(ma[1])-1) * 0.5
        if ma[1] == '4':
            self.diemUT = 0

        self.tong = self.diemUT + d1*2 + d2
        if self.tong >= 18:
            self.kq = "TRUNG TUYEN"
        else:
            self.kq = "LOAI"
        self.tong = round(self.tong,1)
        pass
        
    def __str__(self) -> str:
        return "{} {} {} {:.1f} {}".format(self.ma, self.ten, self.monhoc, self.tong, self.kq)

if __name__ == '__main__':
    arr = [GiaoVien(input(),input(),float(input()),float(input())) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.tong)    
    for i in arr:
        print(i)

# done