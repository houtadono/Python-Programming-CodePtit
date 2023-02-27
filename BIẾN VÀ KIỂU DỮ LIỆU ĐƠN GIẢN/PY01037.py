
# def dem_uoc_so(n):
#     dem = 1
#     if n%2==0:
#         mu = 0
#         while n%2 == 0:
#             mu+=1
#             n//=2
#         dem *= (mu+1)
#     i = 3
#     while i*i<= n:
#         if n%i == 0:
#             mu = 0
#             while n%i == 0:
#                 mu+=1
#                 n//=i
#             dem *= (mu+1)
#         i+=2
#     if n > 1: dem *= 2     
    
#     return dem

# res = [1, 2, 4, 6, 12, 24]

# def find_all():
#     pre = dem_uoc_so(24)
#     i = 24
#     step = 12
#     while i < pow(10,8):
#         now = dem_uoc_so(i)
#         if now > pre:
#             if step > i - res[len(res)-1] or len(str(i))> len(str(res[len(res)-1])): 
#                 step = i - res[len(res)-1]
#             res.append(i)
#             pre = now
#         i+=step

# find_all()
# print(res)

res = [1, 2, 4, 6, 
        12, 24, 36, 48, 60, 
        120, 180, 240, 360, 720, 840, 
        1260, 1680, 2520, 5040, 7560, 
        10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 
        110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 
        1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 
        10810800, 17297280, 21621600, 32432400, 36756720, 43243200, 64864800, 73513440]


# quick but --- IR --- (cant use numpy here) =)) 
# import numpy as np
# res = np.array(res)
# for _ in range(int(input())):
#     x = int(input())
#     print(  res[(res-x)>=0].tolist()[0])
    # print(int(res[(res-x)>=0][0]))


def lower_bound(x,lst):
    l, r = 0, len(lst)
    while l < r:
        mid = (r+l)//2
        if x <= lst[mid]:
            r = mid
        else:
            l = mid+1
    return lst[l]

# --- TLE ---
# for _ in range(int(input())):
#     print( lower_bound(int(input()),res) )

# --- AC ---
import sys # using stdin is better than using input()... quickk

from bisect import bisect_left # using this like lower_bound but quickk

t, i = int(input()), 0
for x in sys.stdin:
    # print(lower_bound(int(x),res)) # AC with 1.67 s
    print(res[bisect_left(res,int(x))]) # AC with 1.00s
    i+=1
    if i== t: break

# done