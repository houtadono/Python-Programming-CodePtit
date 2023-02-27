
for _ in range(int(input())):
    res = ""
    num = 0
    for i in input():
        if i.isdigit():
            num += int(i)
        else:
            res += i
    res = ''.join(sorted(res))
    res+=str(num)
    print(res)

# done