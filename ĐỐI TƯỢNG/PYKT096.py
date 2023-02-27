
stt_team = 1
class Team:
    def __init__(self, ten, truong) -> None:
        global stt_team 
        self.ma_team = "Team%02d" %(stt_team)
        stt_team += 1
        self.ten_team = ten
        self.ten_truong = truong
        pass

    def __str__(self) -> str:
        return "{} {}".format(self.ten_team, self.ten_truong)

stt_ts = 1
class ThiSinh():
    def __init__(self, ten, team):
        global stt_ts
        self.ma = "C%03d" %(stt_ts)
        stt_ts += 1
        self.ten = ten
        self.team = team
        
    def __str__(self):
        return "{} {} {} ".format(self.ma, self.ten, self.team)
    

if __name__ == "__main__":
    arrT = [Team(input(), input()) for _ in range(int(input()))]
    arrTS = []
    for _ in range(int(input())):
        ten, ma_team = input(), input()
        for i in arrT:
            if i.ma_team == ma_team:
                arrTS.append(ThiSinh(ten,i))
                break
    arrTS.sort(key= lambda e: e.ten)
    for i in arrTS:
        print(i)

# done