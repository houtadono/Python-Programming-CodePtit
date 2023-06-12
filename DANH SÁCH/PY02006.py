
def check(a,b,n):
	for i in range(n):
		if a[i] > b[i]: return False
	return True

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    if check(a,b,n):
        print("YES")
    else:
        print("NO")

# done