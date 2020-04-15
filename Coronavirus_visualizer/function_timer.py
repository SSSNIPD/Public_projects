import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time:", round(total*10, 8))
        return rv
    return wrapper

