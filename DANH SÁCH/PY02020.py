
input()
arr = list(map(float, input().split()))

res = list(filter(lambda x: x!=max(arr) and x!=min(arr), arr))

print("%.2f" %(sum(res)/len(res)))

# done