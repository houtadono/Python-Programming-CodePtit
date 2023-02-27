
class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3) -> None:
        self.ten = ten
        self.ns = ns
        self.tong = d1+d2+d3
        pass

    def __str__(self) -> str:
        return "%s %s %.1f" %(self.ten, self.ns, self.tong)

if __name__ == '__main__':
    a = ThiSinh(input(),input(),float(input()),float(input()),float(input()))
    print(a)

# done