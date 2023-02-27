
def generate(i, s, n2, n3, n5, n7):
    if n2*n3*n5*n7 != 0 and s[-1] != '2':
        print(s)
    if i == n:
        return
    i+=1
    generate(i, s+'2', n2+1, n3, n5, n7)
    generate(i, s+'3', n2, n3+1, n5, n7)
    generate(i, s+'5', n2, n3, n5+1, n7)
    generate(i, s+'7', n2, n3, n5, n7+1)


n = int(input())

generate(0, '', 0, 0, 0, 0)

# done