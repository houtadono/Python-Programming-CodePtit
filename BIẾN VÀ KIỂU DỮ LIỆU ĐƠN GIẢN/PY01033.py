# pyright: reportUndefinedVariable=false
import math

l, r = map(int,input().split(' '))

arr = [None]*3
def ql(n,start):
    if n==3:
        if math.gcd(arr[0],arr[1]) == math.gcd(arr[2],arr[1]) == math.gcd(arr[0],arr[2]) == 1:              
            print(f"({arr[0]}, {arr[1]}, {arr[2]})")
        return
    for i in range(start,r+1,1):
        arr[n] = i
        ql(n+1,i)

ql(0,l)
# done