s1 = input().lower().split(' ')
s2 = input().lower().split(' ')

union = sorted(set(s1+s2))
intersection = sorted(set([i for i in s1 if i in s2]))

for i in union:
    print(i,end=' ')

print()
for i in intersection:
    print(i,end=' ')

# done