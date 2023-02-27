
from itertools import permutations
n = input()
res = list(permutations(n))
for i in res:
    print(''.join(i))
    
# done