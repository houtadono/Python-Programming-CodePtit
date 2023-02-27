
from datetime import datetime

class MonHoc:
    def __init__(self, ma_mh, ten_mh) -> None:
        self.ma_mh = ma_mh
        self.ten_mh = ten_mh
        pass

    def __str__(self) -> str:
        return "{} {}".format(self.ma_mh, self.ten_mh)


stt = 1
class CaThi():

    def __init__(self, ngay, gio, nhom, mh):
        self.thoigian = ' '.join([ngay,gio])
        self.nhom = nhom
        self.mh = mh
        global stt 
        self.ma = "T%03d" %(stt)
        stt+=1

    def __str__(self):
        return "{} {} {} {} ".format(self.ma, self.mh, self.thoigian, self.nhom)
    
    def __lt__(self, obj):
        n1 = datetime.strptime(self.thoigian, "%d/%m/%Y %H:%M")
        n2 = datetime.strptime(obj.thoigian, "%d/%m/%Y %H:%M")
        if n1 == n2:
            return str(self.mh) < str(obj.mh)
        return n1 < n2

if __name__ == "__main__":
    n, m = map(int, input().split())
    arrMH = [MonHoc(input(),input()) for _ in range(n)]
    arrCT = []
    for _ in range(m):
        ma_mh, ngay, gio, nhom = input().split()
        for i in arrMH:
            if i.ma_mh == ma_mh:
                arrCT.append(CaThi(ngay,gio,nhom, i))
                break

    arrCT.sort()
    for i in arrCT:
        print(i)

# done