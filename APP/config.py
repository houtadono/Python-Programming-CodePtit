import string
import re

INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"
r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))

def khongdau(utf8_str):
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
