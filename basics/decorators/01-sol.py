import time
t = time.localtime()

def timer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"{res} is the current time"
    return wrapper
    
@timer
def time_now():
    return f"{t.tm_hour}:{t.tm_min}"

print(time_now())