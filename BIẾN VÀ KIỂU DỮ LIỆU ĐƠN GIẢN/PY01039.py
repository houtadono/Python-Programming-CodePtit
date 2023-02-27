
def check(n):
    if len(set(n)) != 2:
        return False
    if len(set([n[i] for i in range(len(n)) if i&1==0])) == 1 and len(set( [n[i] for i in range(len(n)) if i&1==1]) ) == 1:
        return True
    return False

for _ in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")

# done