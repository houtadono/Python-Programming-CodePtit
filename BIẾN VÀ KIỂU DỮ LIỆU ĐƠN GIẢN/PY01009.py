
s = input()
s1 = s.lower()

if len([1 for i in range(len(s)) if s[i] == s1[i] ]) * 2 >= len(s1):
    print(s1)
else:
    print(s.upper())

# done