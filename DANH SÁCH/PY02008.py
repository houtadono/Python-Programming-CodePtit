
from math import sqrt
n, x = map(int, input().split())

N = 10**6
sang = [0]*(N+1)

dem = 0
print(x,end=' ')
for i in range(2, int(sqrt(N))+1):
    if sang[i] == 0:
        x = x+i
        print(x,end=' ')
        dem+=1

        if dem == n:
            break
        for j in range(i*i,N,i):
            sang[j] = 1

# done