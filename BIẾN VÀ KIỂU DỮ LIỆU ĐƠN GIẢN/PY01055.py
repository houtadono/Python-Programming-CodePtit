
def check(n):
    if len(n)&1 == 0 or n[0]==n[1]:
        return False
    return 1 == len(set(map(lambda x: x==n[0] ,n[::2])))

for _ in range(int(input())):
    if check(input()):
        print("YES")
    else:
        print("NO")

# done