
res = []

def generate( i, s, nA, nB, nC):
    if nA > 0 and nA <= nB and nB <= nC:
        res.append(s)
    if i == n: return
    i += 1
    generate( i, s+'A', nA+1, nB, nC)
    generate( i, s+'B', nA, nB+1, nC)
    generate( i, s+'C', nA, nB, nC+1)

n = int(input())
generate(0,"",0,0,0)

for i in sorted(res,key= lambda s: len(s)):
    print(i)

# done