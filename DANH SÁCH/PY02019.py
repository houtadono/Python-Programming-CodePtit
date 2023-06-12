
from math import gcd
n = int(input())
a = sorted(list(map(int, input().split())))

for i in range(n):
	for j in range(i+1,n):
		if(gcd(a[i],a[j]) == 1): print(a[i],a[j])

# done