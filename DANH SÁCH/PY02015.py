
from bisect import bisect_left

N = 10**5
sang = [0]*(N+1)
nto = []

def sang_nguyen_to():
    i = 2
    brk = False
    while i*i < N:
        if sang[i] == 0:
            nto.append(i)
            if brk:
                break
            if i > max_arr and brk == False:
                brk = True
                
            for j in range(i*i, N, i):
                sang[j] = 1
        i+=1

def calculate_step(x):
    index = bisect_left(nto,x)
    return min(nto[index] - x, x - nto[index-1])

n = int(input())
arr = list(map(int, input().split()))
max_arr = max(arr)

sang_nguyen_to()

print(max(map(lambda i: calculate_step(i), arr)))

# done