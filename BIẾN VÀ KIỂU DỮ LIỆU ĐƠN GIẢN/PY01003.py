def lam_tron(n):
    arr = [int(i) for i in str(n)]
    
    for i_index in range(len(arr)-1,0,-1):
        if arr[i_index] > 4:
            arr[i_index-1]+=1
        arr[i_index] = 0

    return int(''.join([str(i_digit) for i_digit in arr])) 

for _ in range(int(input())):
    n = int(input())
    print(lam_tron(n))

# done