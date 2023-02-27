
import math

def ngto(n):
    if n==2: return True
    if n<2 or n % 2 == 0: return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            k+=1
    if ngto(k): 
        print("YES")
    else: 
        print("NO")

# done