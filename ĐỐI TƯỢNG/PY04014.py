
stt = 1
class HocSinh:
    def __init__(self, ten, diem) -> None:
        global stt
        self.ma = "HS%02d" %(stt)
        self.ten = ten
        data = list(map(float, diem.split()))
        data.extend(data[:2])
        self.dtb = sum(data)/12
        self.dtb = round(self.dtb*100+1)/100
        if self.dtb >= 9: self.loai = "XUAT SAC"
        elif self.dtb >=8: self.loai = "GIOI"
        elif self.dtb >=7: self.loai = "KHA"
        elif self.dtb >=5: self.loai = "TB"
        else: self.loai = "YEU"
        stt+=1  
        pass

    def __lt__(self, obj):
        if self.dtb == obj.dtb:
            return self.ma < obj.ma
        return self.dtb > obj.dtb

    def __str__(self) -> str:
        return "{0} {1} {2:.1f} {3}".format(self.ma, self.ten, self.dtb, self.loai)

if __name__ == '__main__':
    t = int(input())
    ds = []
    while t>0:
        t-=1
        ds.append(HocSinh(input(),input()))
    ds.sort()
    for i in ds:
        print(i)

# done
