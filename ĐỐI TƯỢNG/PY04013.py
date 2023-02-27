

stt = 1
class DoLuongMua:
    def __init__(self, ten) -> None:
        global stt
        self.ma = "T%02d" %(stt)
        self.ten = ten
        self.lm = 0
        self.time = 0
        stt+=1
        pass

    def setdata(self, start, end, value):
        start = list(map(int, start.split(':')))
        end = list(map(int, end.split(':')))
        self.time += (end[0]*60 + end[1] - start[0]*60 - start[1])/60
        self.lm += value
    
    def __str__(self) -> str:
        self.lmtb = self.lm/self.time
        return "{0} {1} {2:.2f}".format(self.ma, self.ten, self.lmtb)

if __name__ == '__main__':
    t = int(input())
    ds = []
    while t>0:
        t-=1
        ten = input()
        check = None
        for i in ds:
            if i.ten == ten:
                check = i
                break
        if check != None:
            check.setdata(input(),input(),int(input()))
        else:
            a = DoLuongMua(ten)
            a.setdata(input(),input(),int(input()))
            ds.append(a)
    for i in ds:
        print(i)

# done