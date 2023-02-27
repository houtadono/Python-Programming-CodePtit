
s = input()
if len(s) == 1:
    print(s)

while len(s)>1:
    s = str(int(s[:len(s)//2])+int(s[len(s)//2:]))
    print(s)

# done