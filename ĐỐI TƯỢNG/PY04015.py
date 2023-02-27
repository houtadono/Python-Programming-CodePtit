
stt=1
class HoaDon:
    def __init__(self, ten, sod, soc) -> None:
        global stt
        self.ma = "KH%02d" %(stt)
        stt+=1
        self.ten = ten
        self.cs = soc-sod
        if self.cs > 100:
            self.tt = ((self.cs-100)*200 + 100*50+50*150)*1.05
        elif self.cs > 50:
            self.tt = (100*50 + (self.cs - 50)*150)*1.03
        else:
            self.tt = self.cs*100*1.02
        self.tt = round(self.tt)
        pass
    
    def __lt__(self, obj):
        return self.tt>obj.tt

    def __str__(self) -> str:
        return f"{self.ma} {self.ten} {self.tt}"

arr = []
for _ in range(int(input())):
    arr.append(HoaDon(input(),int(input()),int(input()))) 
arr.sort()
for i in arr:
    print(i)

# done