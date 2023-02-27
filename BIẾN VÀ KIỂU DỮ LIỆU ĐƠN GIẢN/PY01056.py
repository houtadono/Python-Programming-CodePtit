
import math

def nguyen_to(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0 : return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i ==0: 
            return False
    return True

def check(n):
    sum = 0
    for i in range(len(n)):
        if (int(n[i]) - i) % 2 != 0:
            return False
        sum += int(n[i])
    return nguyen_to(sum)

for _ in range(int(input())):
    if check(input()):
        print("YES")
    else:
        print("NO")

# done