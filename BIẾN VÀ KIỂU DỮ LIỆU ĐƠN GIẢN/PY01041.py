
def convert(sub):
    return '1' if sub>0 else '1' if sub==2 else '0'

for _ in range(int(input())):
    n = input()
    x = ''.join(map(lambda i,j: convert(int(i) - int(j))  ,n[1:],n[:-1]))
    if '2' in x or '01' in x or len(n) < 3: 
        # 2 : bằng nhau
        # 01: giảm rồi tăng
        print("NO")
    else:
        print("YES")

# done