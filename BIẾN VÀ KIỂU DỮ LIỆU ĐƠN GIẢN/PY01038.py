
def solve(n):
    for i in range(1001):
        if n % 7 == 0:
            return n
        n = n + int(str(n)[::-1])
    return -1

for _ in range(int(input())):
    print(solve(int(input())))

# done