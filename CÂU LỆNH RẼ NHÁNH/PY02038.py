
from math import factorial

n = int(input())
arr = []
res = 0

def calculate_combination(n,k):
    if k > n: return 0
    return factorial(n) // factorial(k) // factorial(n-k)

for _ in range(4):
    line = list(input())
    res += calculate_combination(line.count('C'),2)
    arr.append(line)

for i in range(4):
    col = [row[i] for row in arr]
    res += calculate_combination(col.count('C'),2)

print(res)

# done