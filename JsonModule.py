# JSON - JAVA SCRIPT OBJECT NOTATION
import json

data = '{"var1" : "Harry", "var2" : 56}'
parsed = json.loads(data)
# json is a dictionary.

print(type(parsed))
print(parsed)

data2 = {
    "cars" : ["Lambo","ferrari"],
    "mobile" : "Iphone",
    "Guitar" : ("Epiphone", "Gibson"),
    "false" : False
}

i = json.dumps(data2) # it converts into Javascript compatible.
print(i)