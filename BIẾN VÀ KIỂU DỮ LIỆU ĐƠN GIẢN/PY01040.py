
from string import ascii_uppercase

DICTS = dict(zip(ascii_uppercase, range(len(ascii_uppercase))))

def devide(s):
    n = len(s)//2
    return s[:n], s[n:]

def rotate(d):
    value_rotate = sum(map(lambda i: DICTS[i], d))
    return ''.join(map(lambda i: ascii_uppercase[(DICTS[i] + value_rotate) % len(DICTS)], d))

def merge(r1, r2):
    return ''.join(map(lambda i1, i2: ascii_uppercase[(DICTS[i1] + DICTS[i2]) % len(DICTS)], r1, r2))

for _ in range(int(input())):
    s = input()
    d1, d2 = devide(s)
    r1, r2 = rotate(d1), rotate(d2)
    m = merge(r1, r2)
    print(m)

# done