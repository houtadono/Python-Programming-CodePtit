
import math

n, k = map(int,input().split(' '))
count = 0
for i in range(pow(10,k-1), pow(10,k)):
    if math.gcd(n,i) == 1:
        count+=1
        print(i,end=' ')
        if count%10 == 0:
            print()

# done        