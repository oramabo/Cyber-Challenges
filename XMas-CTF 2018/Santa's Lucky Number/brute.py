from urllib import request, error

WEBSITE = "http://199.247.6.180:12005/?page="


def find_xmas():
    x = 0
    while True:
        try:
            html = request.urlopen(WEBSITE + str(x))
            ps = html.read().decode("utf-8")
            b = ps.find("<p align=\"center\">", ps.find("<p align=\"center\">") + 1)
            e = ps.find("</p>", ps.find("</p>") + 1)
            val = str(ps[b + 19:e])
            if val.find("X-MAS") != -1:
                print(val)
                break
        except error.URLError as err:
            print(err)
        x += 1


def main():
    find_xmas()


main()
