
res = []

def find_all():
    queue = ['1','2']
    dem = 0
    while dem < 1001:
        k = str(queue.pop(0))
        if 2 * k.count('2') > len(k):
            dem+=1
            res.append(k)
        queue.append(k+'0')
        queue.append(k+'1')
        queue.append(k+'2')

find_all()
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(res[i], end=' ')
    print()

# done