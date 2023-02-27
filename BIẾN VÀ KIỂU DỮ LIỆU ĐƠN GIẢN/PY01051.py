
for _ in range(int(input())):
    m = str(sum(map(int,input())))
    if len(m)>1 and m == m[::-1]:
        print("YES")
    else:
        print("NO")

# done