import time
from functools import lru_cache

@lru_cache(maxsize=3)
def work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("running some work")
    work(3)
    print("done")
    work(3)
    print("called again")
    work(3)
    print("again")
    