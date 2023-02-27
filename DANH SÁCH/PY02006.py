
for _ in range(int(input())):
    n = input()
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    if a <= b:
        print("YES")
    else:
        print("NO")

# done