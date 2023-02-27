
from string import ascii_lowercase

def check(s):
    if not str(s).endswith('.py'):
        return False
    key = ascii_lowercase+'_'
    for i in s[:-3]:
        if i not in key:
            return False
    return True

s = input().lower()
if check(s):
    print("yes")
else:
    print("no")

# done