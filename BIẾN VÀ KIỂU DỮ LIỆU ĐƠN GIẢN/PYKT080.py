
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arrX = [-1,-1,-1, 0, 0, 1, 1, 1]
arrY = [-1, 0, 1,-1, 1,-1, 0, 1]
vs = [[False for i in range(m)] for j in range(n)]

sum = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            for addX,addY in zip(arrX,arrY):
                newI, newJ = addX + i, addY + j
                if newI>=0 and newI<n and newJ>=0 and newJ<m and vs[newI][newJ] == False:
                    vs[newI][newJ] = True
                    sum += arr[newI][newJ]
print(sum)

# done