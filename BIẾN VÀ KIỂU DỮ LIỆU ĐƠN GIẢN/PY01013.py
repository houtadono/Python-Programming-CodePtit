import math

def nguyen_to(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0 : return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i ==0: 
            return False
    return True

def tongcs(n):
    return sum([int(i) for i in str(n)])

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    if nguyen_to(tongcs(math.gcd(a,b))):
        print("YES")
    else:
        print("NO")

# done