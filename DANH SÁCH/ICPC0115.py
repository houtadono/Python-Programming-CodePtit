
from math import factorial

for _ in range(int(input())):
    n = input()
    if int(n) == sum(map(lambda i: factorial(int(i)),n)):
        print("Yes")
    else:
        print("No")

# done