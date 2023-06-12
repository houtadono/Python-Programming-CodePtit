
def isPrime(n):
    if n == 2: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**1/2)+1,2):
        if n%i==0:
            return False
    return True

input()
arr = list(map(int, input().split()))
primes = sorted([x for x in arr if isPrime(x)])
primes_index = 0
for i in range(len(arr)):
    if isPrime(arr[i]):
        arr[i] = primes[primes_index]
        primes_index+=1
print(*arr)

# done