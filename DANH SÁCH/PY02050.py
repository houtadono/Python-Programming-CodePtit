
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = [-1]
    for i in range(n):
        while stack[-1] != -1 and arr[i] > arr[stack[-1]]:
            stack.pop()
        print(i - stack[-1], end=' ')
        stack.append(i)
    print()

# done