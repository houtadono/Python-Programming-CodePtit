
import re

def chuanHoaTen(ten):
    return re.sub("\\s+"," ", ten.strip()).title()

stt = 1
class KhachHang:
    def __init__(self, ten, line2) -> None:
        global stt
        self.ma = "KH%02d" %(stt)
        stt+=1
        self.ten = chuanHoaTen(ten)
        loaiho, csdau, cscuoi = line2
        if loaiho == 'A':
            dm = 100
        elif loaiho == 'B':
            dm = 500
        else:
            dm = 200
        cssd = int(cscuoi) - int(csdau)
        if cssd < dm:
            self.trongdm = cssd * 450
            self.vuotdm = 0
            self.thue = 0
        else:
            self.trongdm = dm * 450
            self.vuotdm = (cssd - dm) * 1000
            self.thue = self.vuotdm//20
        self.phainop = self.trongdm+self.vuotdm+self.thue
        pass

    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.trongdm, self.vuotdm, self.thue, self.phainop)
        pass

if __name__ == '__main__':
    arr = [KhachHang(input(),input().split()) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.phainop)
    for i in arr:
        print(i)

# done