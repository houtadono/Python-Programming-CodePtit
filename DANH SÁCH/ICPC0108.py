
def find_sum_triple_zero(arr, n):
    res = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while l<r:
            if arr[i]+arr[l]+arr[r] == 0:
                res +=1
                l +=1
            elif arr[i]+arr[l]+arr[r] > 0:
                r -=1
            else:
                l+=1
    return res    

for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(find_sum_triple_zero(arr,n))

# done