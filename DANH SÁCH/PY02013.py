
while 1:
    n = int(input())
    if n == 0:
        break
    dem = 1
    while n!=1:
        if n&1==0:
            n//=2
        else:
            n = n*3 + 1
        dem+=1
    print(dem)

# done