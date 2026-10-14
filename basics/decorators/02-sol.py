import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} is called in {end - start} sec")
    return wrapper

@timer
def time_sleep(n):   
    time.sleep(n)
    # print('time to sleep')

time_sleep(2)