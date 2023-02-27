
nto = [1] * 501
nto[0] = nto[1] = 0

def sang_nguyen_to():
    i = 2
    while i*i < 501:
        if nto[i] == 1 :
            for j in range(i*i, 501, i):
                nto[j] = 0
        i+=1

def check(n):
    for i in range(len(n)):
        if nto[i] + nto[int(n[i])] == 1:
            return False
    return True

sang_nguyen_to()
for _ in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")

# done