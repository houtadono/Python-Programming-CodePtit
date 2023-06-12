
def uni(a,b,c):
    res = []
    x = y = z = 0
    while x < len(a) and y < len(b) and z < len(c):
        if a[x] == b[y] and b[y] == c[z]:
            res.append(a[x])
            x+=1
            y+=1
            z+=1
        elif a[x] <= b[y] and a[x] <= c[z]:
            x+=1
        elif b[y] <= a[x] and b[y] <= c[z]:
            y+=1
        elif c[z] <= a[x] and c[z] <= b[y]:
            z+=1        

    return res

for t in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    res = uni(a,b,c)
    if len(res) > 0: print(*res)
    else: print("NO")
    
# done