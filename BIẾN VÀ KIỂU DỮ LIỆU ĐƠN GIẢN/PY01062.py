
from collections import Counter
from math import sqrt

def nguyen_to(n):
    if n == 2 : return True
    if n < 2 or n%2 == 0: return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = input()
    if not nguyen_to(len(n)):
        print("NO")
        continue
    d = Counter(n)
    if (d['2']+d['3']+d['5']+d['7'])*2 > len(n):
        print("YES")
    else:
        print("NO")

# done