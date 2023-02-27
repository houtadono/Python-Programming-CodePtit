
import math

def ngto(n):
    if n==2: return True
    if n<2 or n % 2 == 0: return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

def find_solve(arr):
    for i in range(len(arr)):
        if ngto(sum(arr[:i+1])) and ngto(sum(arr[i+1:])):
            return i
    return "NOT FOUND"

input()
arr = list(set(map(int, input().split())))
print(find_solve(arr))

# empty