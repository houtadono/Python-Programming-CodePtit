
n, m = map(int, input().split(' '))

arr = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))

arrX = [-1,-1,-1, 0, 0, 1, 1, 1]
arrY = [-1, 0, 1,-1, 1,-1, 0, 1]
vs = [[False]*m]*n

sum = 0
for i in range(n):
    for j in range(m):
        print(arr[i][j],end= " ")
        if arr[i][j] == -1:
            for addX,addY in zip(arrX,arrY):
                newI, newJ = addX + i, addY + j
                if vs[newI][newJ] == False:
                    vs[newI][newJ] = True
                    # print(arr[newI][newJ])
                    sum += arr[newI][newJ]
    print()
print(sum)

# done