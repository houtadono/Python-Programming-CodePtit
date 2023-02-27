
import math

def ngto(n):
    if n==2: return True
    if n<2 or n % 2 == 0: return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())

for _ in range(n):
    for i in map(int, input().split()):
        if ngto(i):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()

# done