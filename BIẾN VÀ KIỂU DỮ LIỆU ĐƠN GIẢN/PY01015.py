
def so_khong_giam(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

for _ in range(int(input())):
    s = input()
    if so_khong_giam(s):
        print("YES")
    else:
        print("NO")

# done