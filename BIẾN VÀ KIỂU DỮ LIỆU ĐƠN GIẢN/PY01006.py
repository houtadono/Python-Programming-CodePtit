
for _ in range(int(input())):
    n = input()
    count47 = n.count('4') + n.count('7')
    if count47 == len(n):
        print("YES")
    else:
        print("NO")

# done