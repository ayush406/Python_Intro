import requests

r = requests.get("https://www.w3schools.com/python/module_requests.asp")
# print(r.text)

u = "https://www.w3schools.com/python/module_requests.asp"
data = {
    "p1" : 4,
    "p2" : 8
}

r1 = requests.post(url=u, data = data)
print(r1.text)