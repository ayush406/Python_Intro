Dict = {"Canada" : "Best", "Germany" : "Good", "USA" : "woo"}

print(Dict)
print(Dict["Canada"])

#nested-Dictionary
Dict1 = {"Canada" : "Best", "Germany" : "Good", "USA" : {"MS" : "DSC", "MIM" : "UBC"}}
print(Dict1["USA"]["MIM"])
Dict1["UK"] = "Leeds" # to add an item in a dictionary
del Dict1["Canada"] # to remove an entry
print(Dict1)

# use .copy() function instead of assignment operator.

Dict2 = Dict1.copy()

print(Dict1.keys())
print(Dict1.items())
