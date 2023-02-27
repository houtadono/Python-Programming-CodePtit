
a, k, n = map(int,input().split(' '))
x = n - a 

b = k - (a%k)
if b > x:
    print(-1)
else:
    while b <= x:
        print(b,end=" ")
        b+=k
# done