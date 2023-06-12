import re
res = []
for _ in range(int(input())):
    res.extend(map(int,re.findall(r'\d+', input())))
res.sort()
for i in res:
    print(i)

# done