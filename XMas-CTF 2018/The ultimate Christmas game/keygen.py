import hashlib
from itertools import product
from string import ascii_letters, digits

counter = 1

while True:
    for x in product(ascii_letters + digits, repeat=counter):
        brute = ''.join(x)
        if hashlib.md5(brute.encode("utf8")).hexdigest()[:5] == "f292d":
            print(brute)
            break
    else:
        counter += 1
        continue
    break
