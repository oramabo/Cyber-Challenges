import urllib.request

WEBSITE = "http://45.76.90.207:12000/?guess=1"
LIST = []

for i in range(20):
    mini = []
    for j in range(20):
        try:
            html = urllib.request.urlopen(WEBSITE)
            ps = html.read().decode("utf-8")
            b = ps.find("The Monolith desired:<br>")
            e = ps.find("<br><br><br><p ")
            mini.append(int(ps[25 + b:e]))
        except urllib.error.URLError as err:
            print(err)
    LIST.append(mini)

for k in LIST:
    print(k)
