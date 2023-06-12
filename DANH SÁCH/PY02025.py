
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = set(a)
B = set(b)

intersection = sorted(list(A & B))
A_diff_B = sorted(list(A - B))
B_diff_A = sorted(list(B - A))

print(*intersection)
print(*A_diff_B)
print(*B_diff_A)

# done