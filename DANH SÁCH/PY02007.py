
a = []
while 1:
    a.extend(map(int, input().split()))
    if len(a) == 10: 
        break
print(len(set(map(lambda i: i%42,a))))

# done