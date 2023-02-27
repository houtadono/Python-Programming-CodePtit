
import re

def chuanHoaTen(ten):
    return re.sub("\\s+"," ", ten.strip()).title()
    
stt = 1
class SinhVien:
    def __init__(self, ten, d1, d2, d3) -> None:
        global stt
        self.ma = "SV%02d" %(stt)
        stt+=1
        self.ten = chuanHoaTen(ten)
        self.dtb = round((d1*3+d2*3+d3*2)/8  + 0.0000000001,2)
        self.xh = 0
        
    def __str__(self) -> str:
        return "{} {} {:.2f} {}".format(self.ma, self.ten, self.dtb, self.xh)

if __name__ == '__main__':
    arr = [SinhVien(input(),float(input()),float(input()),float(input())) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.dtb) 
    for i in range(len(arr)):
        if arr[i].dtb == arr[i-1].dtb and i > 0:
            arr[i].xh = arr[i-1].xh
        else:
            arr[i].xh = i+1
        print(arr[i])

# done