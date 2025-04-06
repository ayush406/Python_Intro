Dict = {"Canada" : "Best", "Germany" : "Good", "USA" : "woo"}

for i, j in Dict.items():
    print(i,j)

lis = [8, 9, 1, 2, "ayush", "hdjk"]

for i in lis:
    if str(i).isnumeric() and i >6:
        print(i)