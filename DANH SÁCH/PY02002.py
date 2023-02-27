
from array import array
res = [0]*93
def find_all():
    res[0] = 0
    res[1] = 1
    for i in range(2,93):
        res[i] = res[i-1] + res[i-2]
find_all()

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a,b+1):
        print(res[i],end=' ')
    print()

# done