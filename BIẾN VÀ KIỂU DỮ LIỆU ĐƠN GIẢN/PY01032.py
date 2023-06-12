
l, r, n = map(int, input().split())

if n == 2:
    start = False
    res = 2 - l
    if res < 0: res = 0
    end = False
    q = []
    q.append('1')
    while end == False:
        top = q.pop(0)
        s = top + top[::-1]
        s = int(s,2)
        if start == False:
            if s >= l: 
                start = True
        else:
            if s > r:
                end = True
            res+=1
            
        if end == False:
            s0 = int(top +'0'+ top[::-1],2)
            s1 = int(top +'1'+ top[::-1],2)
            if s0>=l and s0<=r:
                res+=1
            if s1>=l and s1<=r:
                res+=1
        q.append(top+'0')
        q.append(top+'1')
    print(res)

if n==3:
    res = 0
    if l == 0: res += 1
    if l <= 1 and 1 <= r:
        res += 1
    if l<=6643 and 6643<=r: # 1000 1 0001
        res += 1
    if l <= 1422773 and 1422773 <= r: # 220 002 1 200 022
        res += 1
    print(res)

if n>3:
    res = 0
    if l == 0: 
        res += 1
    if l<= 1 and 1<= r:
        res += 1
    print(res)

# done