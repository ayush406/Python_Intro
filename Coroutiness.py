def search():
    import time
    book = "this is a very good book."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Verified")
        else:
            print("Not present")


s = search()
next(s)
s.send("bgv")