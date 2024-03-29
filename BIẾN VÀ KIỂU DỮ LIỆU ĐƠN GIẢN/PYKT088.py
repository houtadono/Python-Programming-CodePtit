def count(n):
	res = 0
	limit = int(n**0.5)
	prime = [i for i in range(limit+1)]
	i = 2
	while i*i <= limit:
		if prime[i] == i:
			for j in range(i*i,limit+1,i):
				if prime[j] == j:
					prime[j] = i
		i += 1
	
	for i in range(2, limit+1):
		p = prime[i]
		q = prime[i//p]
		if p*q == i and q != 1 and p != q: res+=1
		elif prime[i] == i and i**8 <= n: res+=1
	return res

n = int(input())
print(count(n))

# done