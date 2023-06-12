import re

def is_valid_ip(ip):
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
        return False
    for num in ip.split('.'):
        if int(num) < 0 or int(num) > 255:
            return False
    return True

for _ in range(int(input())):
    print("YES") if is_valid_ip(input()) else print("NO")

# done