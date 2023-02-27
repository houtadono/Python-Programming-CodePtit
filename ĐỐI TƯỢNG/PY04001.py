
from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def distance(self, p):
        return "%.4f" %(sqrt( (self.x - p.x)**2 + (self.y - p.y)**2 ))

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

# done