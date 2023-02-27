
import math

for _ in range(int(input())):
    a = input()
    b = a[::-1]
    if math.gcd(int(a),int(b)) == 1:
        print("YES")
    else:
        print("NO")

# done 