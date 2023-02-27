
n, step = input(), 0
if n[0] == '-':
    n = sum(map(int, n[1:])) - 3
    step += 1
n = int(n)

while n > 9:
    n = sum(map(int, str(n)))
    step += 1

print(step)

# done