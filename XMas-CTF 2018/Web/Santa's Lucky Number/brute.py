import urllib.request
import hashlib
from itertools import product
from string import ascii_letters, digits
import binascii

WEBSITE = "http://199.247.6.180:12005/?page="
# f = open('iterative.txt', 'w')


def alphanumeric():
    counter = 0
    while True:
        for x in product(ascii_letters + digits, repeat=counter):
            i = ''.join(x)
            try:
                html = urllib.request.urlopen(WEBSITE + str(i))
                ps = html.read().decode("utf-8")
                b = ps.find("<p align=\"center\">", ps.find("<p align=\"center\">") + 1)
                e = ps.find("</p>", ps.find("</p>") + 1)
                STRING = str(ps[b + 18:e])
                if STRING.find("4d4153") != -1:
                    print(i, STRING)
                    break
            except urllib.error.URLError as err:
                print(err)
        else:
            counter += 1
            continue
        break


def iterative():
    for x in range(10):
        try:
            html = urllib.request.urlopen(WEBSITE + str(x))
            ps = html.read().decode("utf-8")
            b = ps.find("<p align=\"center\">", ps.find("<p align=\"center\">") + 1)
            e = ps.find("</p>", ps.find("</p>") + 1)
            STRING = str(ps[b + 19:e])
            f.write(str(x) + " " + STRING + " " + str(binascii.unhexlify(STRING)) + "\n")
        except urllib.error.URLError as err:
            f.write(err)


def iterative1():
    x = 0
    while True:
        try:
            html = urllib.request.urlopen(WEBSITE + str(x))
            ps = html.read().decode("utf-8")
            b = ps.find("<p align=\"center\">", ps.find("<p align=\"center\">") + 1)
            e = ps.find("</p>", ps.find("</p>") + 1)
            STRING = str(ps[b + 19:e])
            if STRING.find("X-MAS") != -1:
                print(STRING)
                break
        except urllib.error.URLError as err:
            print(err)
        x += 1


def main():
    iterative1()
    # f.close()


main()
