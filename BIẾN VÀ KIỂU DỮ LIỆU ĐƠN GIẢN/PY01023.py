
for _ in range(int(input())):
    n = int(input())
    print(1, end='')
    i = 2
    while i*i <= n:
        if n%i == 0:
            mu = 0
            while n%i == 0:
                n //= i
                mu+=1
            print(f" * {i}^{mu}", end='')
        i += 1
    if n > 1 :
        print(f" * {n}^1", end='')
    print()
# up: u can divide n by 2 first and i start = 3, step = 2 in loop
# done