
class Rectangle:
    def __init__(self, w, h, c) -> None:
        self.width = w
        self.height = h
        self.co = str(c).title()
    
    def perimeter(self):
        return (self.width+self.height)*2

    def area(self):
        return self.width*self.height
    
    def color(self):
        return self.co


if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

# done