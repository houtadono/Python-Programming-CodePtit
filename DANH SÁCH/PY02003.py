
from bisect import bisect_left
 
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
    
hamming = [0]*(10**5+1)

def find_all():
    save2 ,i2= 2, 0
    save3 ,i3= 3, 0
    save5 ,i5= 5, 0
    hamming[0] = 1
    for i in range(1,10**5):
        hamming[i] = min(save2,save3,save5)
        if hamming[i] == save2:
            i2 += 1
            save2 = hamming[i2] * 2
        if hamming[i] == save3:
            i3 += 1
            save3 = hamming[i3] * 3
        if hamming[i] == save5:
            i5 += 1
            save5 = hamming[i5] * 5

find_all()
for _ in range(int(input())):
    x = int(input())
    k = BinarySearch(hamming,x)
    print(k+1) if k!=-1 else print("Not in sequence")

# done