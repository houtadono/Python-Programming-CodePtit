
for _ in range(int(input())):
    s = input()
    n = len(s) - 1
    while s[n] >= s[n-1] and n>0:
        n-=1
    if n == 0 or (n == 1 and s[1] == '0'):
        print(-1)
        continue
    pos_l = n-1
    pos_r = len(s) - 1
    while s[pos_l] <= s[pos_r] or s[pos_r] == s[pos_r-1]:
        pos_r -= 1

    print(s[:pos_l]+s[pos_r]+s[pos_l+1:pos_r]+s[pos_l]+s[pos_r+1:])

# done