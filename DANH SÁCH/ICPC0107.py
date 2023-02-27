
for _ in range(int(input())):
    p, q = sorted(input().split(' '))

    k = input()
    try:
        x1 = str(int(k))
        x2 = input()
    except:
        x1 ,x2 = k.split(' ')

    x1_l, x2_l = x1.replace(q,p), x2.replace(q,p)
    x1_u, x2_u = x1.replace(p,q), x2.replace(p,q)
    print(int(x1_l)+int(x2_l), int(x1_u)+int(x2_u))

# done