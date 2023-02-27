
import re

def chuanHoaTen(ten):
    return re.sub("\\s+"," ", ten.strip()).title()
    
stt = 1
class ThiSinh:
    def __init__(self, ten, diem, dantoc, kv) -> None:
        global stt
        self.ma = "TS%02d" %(stt)
        stt+=1

        self.ten = chuanHoaTen(ten)
        self.tongdiem = diem
        if dantoc != 'Kinh': self.tongdiem += 1.5
        if kv == '1':
            self.tongdiem += 1.5
        if kv == '2':
            self.tongdiem += 1
        self.kq = "Do" if self.tongdiem >= 20.5 else "Truot"
        
    def __str__(self) -> str:
        return "{} {} {:.1f} {}".format(self.ma, self.ten, self.tongdiem, self.kq)

if __name__ == '__main__':
    arr = [ThiSinh(input(),float(input()),input(),input()) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.tongdiem)    
    for i in arr:
        print(i)

# done