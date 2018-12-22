import urllib.request

WEBSITE = "http://199.247.6.180:12005/?page="


def iterative():
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
    iterative()


main()
