
from sys import stdin
from math import sqrt
from array import array


# still --- TLE ---

n = 2*10**6
res = array('i',[0]*(n+1))
# like: res = [0]*(n+1) and ---MLE-- =)))
# array is more compact in-memory size 

# ta set res[i] = ước số nguyên tố lớn nhất của i
# ex: res[15] = 3
for i in range(2,int(sqrt(n))+1):
    if res[i] == 0:
        res[i] = i
        for j in range(n//i + 1):
            res[i*j] = i

# tính tổng ước số của i: 
# res[i] = ước lớn nhất(res ban đầu) + ước của i/ước lớn nhất (phần này được tính ở trước đó)
# ex: res[15]  = 3 + res[15/3]
# ex: res[12] = 3 + res[12/3] = 3 + res[4] (res[4] được tính trước đó = 2 + res[4/2])

for i in range(4,n+1): 
    res[i] += res[i//res[i]] if res[i] else i

sum = 0
t, it = int(stdin.readline()), 0
while it < t:
    sum += res[int(stdin.readline())]
    it+=1

print(sum)

# --- IR ---
# from sympy.ntheory import factorint
# res =0
# t, it = int(input()), 0
# for x in stdin:
#     d = dict(factorint(int(x)))
#     res += sum(map(lambda i: i * d[i], d.keys()))
#     it+=1
#     if it == t: break
# print(res)

# --- TLE ---
# sum =0
# t, it = int(input()), 0
# for x in stdin:
#     n = int(x)
#     while n % 2 == 0:
#         n//=2
#         sum+=2
#     i = 3
#     while i*i <= n:
#         while n % i == 0:
#             sum += i
#             n//=i
#         i += 2
#     if n > 1: sum+=n
#     it+=1
#     if it == t: break
# print(sum)

# TLE