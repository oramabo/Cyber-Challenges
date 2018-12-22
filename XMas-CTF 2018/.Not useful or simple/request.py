from requests_html import HTMLSession

session = HTMLSession()
URL = "http://199.247.6.180:12004/"

r = session.get(URL)
print(r.html.text)
print(r.html.find('input'))

s = session.post(URL, data="/flag.txt")
print(s.text)
