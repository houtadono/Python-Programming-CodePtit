
res = []

def find_all():
    queue = [2,4,6,8]
    while True:
        a = queue.pop(0)
        if a > 10000: break
        res.append(int(str(a)+str(a)[::-1]))
        for i in [0,2,4,6,8]:
            queue.append(a*10+i)
find_all()

for _ in range(int(input())):
    n = int(input())
    i = 0
    while res[i] < n:
        print(res[i],end=" ")
        i+=1
    print()
    
# done