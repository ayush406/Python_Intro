# normal argument should be at first place and then args.
def funargs(n, *args, **kwargs):
    print(n)
    print(args[0])
    for i in args:
        print(i)

    for j,k in kwargs.items():
        print(f"{j} is a {k}")

# args is for list whereas kwargs is for dictionary.
# args stores the value in form of tuple and kwargs in form of a dictionary.

Dict = {"Canada" : "Best", "Germany" : "Good", "USA" : "woo"}
h = ["ayush", "Rishabh", "Saby", "Rajat"]
funargs("german", *h, **Dict)

