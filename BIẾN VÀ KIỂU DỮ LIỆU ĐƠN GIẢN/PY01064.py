
from string import ascii_uppercase

def get_result(n,k):
    if k == pow(2,n-1):
        return ascii_uppercase[n-1]
    if k > pow(2, n-1):
        return get_result(n-1, k - pow(2, n-1))
    return get_result(n-1, k)

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    print(get_result(n,k))

# done