
from datetime import datetime

class GameThu:
    def __init__(self, ma, ten, giovao, giora):
        self.ma, self.ten = ma, ten
        vao = datetime.strptime(giovao, "%H:%M")
        ra = datetime.strptime(giora, "%H:%M")
        self.thoigian = (ra - vao).seconds
        
    def __str__(self):
        return "{} {} {} gio {} phut".format(self.ma, self.ten, self.thoigian//60//60, self.thoigian//60%60)
    

if __name__ == "__main__":
    arr = [GameThu(input(), input(), input(), input()) for _ in range(int(input()))]
    arr.sort(key = lambda x : -x.thoigian)
    for i in arr:
        print(i)

# done