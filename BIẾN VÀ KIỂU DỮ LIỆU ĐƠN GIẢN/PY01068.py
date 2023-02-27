
def back_tracking(m,pos,res):
    if m == k:
        print(res)
        return
    for i in range(pos,n,1):
        back_tracking(m+1,i+1,res + s[i]+' ')

k = int(input().split(' ')[1])
s = sorted(set(input().split(' ')))
n = len(s)

back_tracking(0,0,"")

# done