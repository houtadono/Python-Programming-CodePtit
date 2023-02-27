
n= int(input())
arr = []
d1 = []
d2 = []
while len(arr) < n: 
    arr.extend(map(int, input().split()))

for i in arr:
	if i%2 == 0: d1.append(i)
	else: d2.append(i)
        
d1.sort()
d2.sort(reverse=True)

i1 = i2 = 0
for i in arr:
    if i&1 == 1:
        print(d2[i2],end=' ')
        i2+=1
    else:
        print(d1[i1],end=' ')
        i1+=1

# done