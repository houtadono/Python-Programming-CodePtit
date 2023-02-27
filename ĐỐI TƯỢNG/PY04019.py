
stt = 1
class ThiSinh:
    def __init__(self, ten, d1, d2) -> None:
        global stt
        if stt < 10:
            self.ma = "TS%02d" %(stt)
        else:
            self.ma = "TS0%02d" %(stt)
            
        stt+=1
        self.ten = ten
        if d1 > 10: d1 /= 10
        if d2 > 10: d2 /= 10
        self.dtb = (d1+d2)/2
        if self.dtb < 5:
            self.xl = "TRUOT"
        elif self.dtb < 8:
            self.xl = "CAN NHAC"    
        elif self.dtb < 9.5:
            self.xl = "DAT"  
        else:
            self.xl = "XUAT SAC" 
        pass
        
    def __str__(self) -> str:
        return "{} {} {:.2f} {}".format(self.ma, self.ten, self.dtb, self.xl)

if __name__ == '__main__':
    arr = [ThiSinh(input(),float(input()),float(input())) for _ in range(int(input()))]
    arr.sort(key= lambda e: -e.dtb)    
    for i in arr:
        print(i)

# done