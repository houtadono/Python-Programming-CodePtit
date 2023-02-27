
while 1:
    n = int(input())
    if n == 0:
        break
    res = []
    while n>0:
        n-=1
        res.append(int(input()))
    res.sort()
    if res[0] == res[-1]:
        print("BANG NHAU")
    else:
        print(f"{res[0]} {res[-1]}")

# done