
for _ in range(int(input())):
    s = input()
    res = ""
    size = 0
    c = ''
    for i in s:
        try:
            size += int(i)
            res = res.ljust(size,c)
        except:
            c = i
    print(res)

# done