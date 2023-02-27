
import re
partern = "\\d+"
for _ in range(int(input())):
    n = input()
    a = list(map(int, re.findall(pattern=partern,string= n)))
    if len(a)>0:
        print(max(a))

# done