
n = int(input())
arr = list(map(int,input().split(' ')))
i = 0
while i < len(arr)-1:
    if (arr[i] + arr[i+1]) &1 == 0:
        del arr[i]
        del arr[i]
        if i > 0: i -= 1
    else:
        i+=1
print(len(arr))

# done