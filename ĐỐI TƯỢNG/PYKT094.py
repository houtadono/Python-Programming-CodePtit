
class PhongBan:
    def __init__(self, pb) -> None:
        self.ma_pb = pb[0]
        self.ten_pb = pb[1]
        pass

    def __str__(self) -> str:
        return "{} {}".format(self.ma_pb, self.ten_pb)

class NhanVien():

    def __init__(self, ma, ten, luongcoban,songaycong, ten_pb):
        self.ma, self.ten, self.ten_pb = ma, ten, ten_pb
        loai_nv = ma[0]
        namcongtac = int(ma[1:3])
        self.luong = luongcoban*songaycong
        if loai_nv == 'A':
            if namcongtac <4:
                self.luong *= 10
            elif namcongtac <9:
                self.luong *= 12
            elif namcongtac <16:
                self.luong *= 14
            else:
                self.luong *= 20    
        elif loai_nv == 'B':
            if namcongtac <4:
                self.luong *= 10
            elif namcongtac <9:
                self.luong *= 11
            elif namcongtac <16:
                self.luong *= 13
            else:
                self.luong *= 16  
        elif loai_nv == 'C':
            if namcongtac <4:
                self.luong *= 9
            elif namcongtac <9:
                self.luong *= 10
            elif namcongtac <16:
                self.luong *= 12
            else:
                self.luong *= 14
        else:
            if namcongtac <4:
                self.luong *= 8
            elif namcongtac <9:
                self.luong *= 9
            elif namcongtac <16:
                self.luong *= 11
            else:
                self.luong *= 13
        pass

    def __str__(self):
        return "{} {} {} {} ".format(self.ma, self.ten, self.ten_pb, self.luong*1000)
    

if __name__ == "__main__":
    arrpb = [PhongBan(input().split(' ',1)) for _ in range(int(input()))]
    arrNV = []
    for _ in range(int(input())):
        ma_nv = input()
        for i in arrpb:
            if i.ma_pb == ma_nv[-2:]:
                arrNV.append(NhanVien(ma_nv,input(),int(input()),int(input()),i.ten_pb))
                break
    for i in arrNV:
        print(i)

# done