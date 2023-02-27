
import math

def nguyen_to(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0 : return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i ==0: 
            return False
    return True

for _ in range(int(input())):
    m = sum(map(int,input()))
    if nguyen_to(m):
        print("YES")
    else:
        print("NO")

# done