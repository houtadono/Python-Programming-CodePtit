
from datetime import datetime

stt_tl = 1
class TheLoai:
    def __init__(self, ten_tl) -> None:
        global stt_tl 
        self.ma_tl = "TL%03d" %(stt_tl)
        self.ten_tl = ten_tl
        stt_tl += 1
        pass

sttP = 1
class Phim(TheLoai):

    def __init__(self, ngay, tenP, sotap, tl):
        self.ngay, self.tenP, self.sotap = ngay, tenP, sotap
        global sttP
        self.maP = "P%03d" %(sttP)
        sttP += 1
        self.ten_tl = tl
        
    def __str__(self):
        return "{} {} {} {} {}".format(self.maP, self.ten_tl, self.ngay, self.tenP, self.sotap)
    
    def __lt__(self, obj):
        n1 = datetime.strptime(self.ngay, "%d/%m/%Y")
        n2 = datetime.strptime(obj.ngay, "%d/%m/%Y")
        if n1 == n2:
            if self.tenP == obj.tenP:
                return self.sotap > obj.sotap
            return self.tenP < obj.tenP
        return n1 < n2

if __name__ == "__main__":
    n, m = map(int, input().split())
    arrTL = [TheLoai(input()) for _ in range(n)]
    arrP = []
    for _ in range(m):
        ma_tl = input()
        for i in arrTL:
            if i.ma_tl == ma_tl:
                arrP.append(Phim(input(),input(),input(),i.ten_tl))
                break

    arrP.sort()
    for i in arrP:
        print(i)

# done