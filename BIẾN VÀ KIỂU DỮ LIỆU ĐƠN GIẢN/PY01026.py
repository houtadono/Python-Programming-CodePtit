
from collections import Counter
for i in range(int(input())):
    s1 = input()
    s2 = input()
    print(f"Test {i+1}: ",end='')
    if Counter(s1) == Counter(s2):
        print("YES")
    else:
        print("NO")

# done