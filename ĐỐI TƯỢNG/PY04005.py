
from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def distance(self, p):
        return sqrt( (self.x - p.x)**2 + (self.y - p.y)**2 )

class Triangle:
    def __init__(self, a, b ,c) -> None:
        self.a, self.b, self.c = a, b, c

    def check(self):
        self.c1 = self.a.distance(self.b)
        self.c2 = self.a.distance(self.c)
        self.c3 = self.b.distance(self.c)
        if self.c1+self.c2 <= self.c3 or self.c1+self.c3<=self.c2 or self.c2+self.c3<=self.c1:
            return False
        return True
    
    def chuvi(self):
        return self.c1+self.c2+self.c3

if __name__ == '__main__':
    t = int(input())
    arr = []
    while 1:
        arr.extend(list(map(float,input().split())))
        if len(arr) >= t*6: break

    for i in range(t):
        p1 = Point(arr[i*6],arr[i*6+1])
        p2 = Point(arr[i*6+2],arr[i*6+3])
        p3 = Point(arr[i*6+4],arr[i*6+5])
        a = Triangle(p1,p2,p3)
        if a.check():
            print("%.3f" %(a.chuvi()))
        else:
            print("INVALID")

# done