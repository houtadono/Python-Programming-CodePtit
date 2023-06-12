from datetime import datetime

class MonThi:
    def __init__(self, ma,ten,hinhThuc) -> None:
        self.ma, self.ten, self.hinhThuc = ma, ten, hinhThuc
        pass
    def __str__(self) -> str:
        return self.ten

class CaThi:
    stt = 1
    def __init__(self, ngayThi, gioThi, phongThi) -> None:
        self.ma = "C%03d" %(CaThi.stt)
        CaThi.stt+=1
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.phongThi = phongThi
        self.time = datetime.strptime(ngayThi+' '+gioThi,"%d/%m/%Y %H:%M")
        pass
    def __str__(self) -> str:
        return self.ngayThi + ' ' + self.gioThi + ' ' + self.phongThi

class LichThi:
    def __init__(self, caThi, monThi, maNhom, soSV) -> None:
        self.caThi = caThi
        self.monThi = monThi
        self.maNhom, self.soSV = maNhom, soSV
        pass
    def __str__(self) -> str:
        return str(self.caThi)+' '+str(self.monThi)+' '+self.maNhom+' '+self.soSV

if __name__ == '__main__':
    with open('MONTHI.in','r') as f:
        dsMonThi = [MonThi(f.readline().strip(), f.readline().strip(), f.readline().strip()) for _ in range(int(f.readline()))]
    with open('CATHI.in','r') as f:
        dsCaThi = [CaThi(f.readline().strip(), f.readline().strip(), f.readline().strip()) for _ in range(int(f.readline()))]

    dsLichThi = []
    with open('LICHTHI.in','r') as f:
        for _ in range(int(f.readline())):
            maCa, maMon, maNhom, soSV = f.readline().strip().split()
            caThi = None
            for i in dsCaThi:
                if i.ma == maCa:
                    caThi = i
                    break
            monThi = None
            for i in dsMonThi:
                if i.ma == maMon:
                    monThi = i
                    break
            dsLichThi.append(LichThi(caThi,monThi,maNhom,soSV))
    
    dsLichThi.sort(key= lambda x: x.caThi.time)
    for i in dsLichThi:
        print(i)

# done