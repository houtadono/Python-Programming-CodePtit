from re import findall
for t in range(int(input())):
	n = int(input())
	s = ' ' + input().replace(' ', '  ') + ' '
	cnt = 0
	sum = 0
	for i in range(-18,19):
		if(cnt >= 3): break
		if i == 0: continue
		str = ' '
		if i < 0: str = '-'
		str += "\\d"*abs(i)
		str += ' '
		x = [int(k) for k in findall(str,s)]
		while cnt < 3 and len(x) > 0:
			it = min(x)
			sum += it
			x.remove(it)
			cnt += 1
	print(sum)

# done