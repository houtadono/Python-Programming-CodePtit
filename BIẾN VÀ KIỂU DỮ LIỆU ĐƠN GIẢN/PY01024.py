
def check(n):
    if sum(n) % 10 != 0: return False
    for i in range(len(n)-1):
        if abs(n[i] - n[i+1]) != 2:
            return False
    return True

for _ in range(int(input())):
    if check( list(map(int, input()))):
        print("YES")
    else:
        print("NO")

# done