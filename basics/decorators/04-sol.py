# import time
# cached_value = []
# def cached(func):
#   def wrapper(*args, **kwargs):
#     res = func(*args, **kwargs)
#     if res in cached_value:
#       # time.sleep(2)
#       return res
#     else:
#       cached_value.append(res)
#       return res
#   return wrapper
       
# @cached
# def actual_value(n):
#   return n

# print(actual_value(2))
# print(actual_value(2))
# print(actual_value(2))
# print(actual_value(3))
# print(actual_value(3))
# print(actual_value(3))


def cache(func):
    cached = {}
    def wrapper(*args):
        if args in cached:
            return cached[args]
        result = func(*args)
        cached[args] = result
        return result
    return wrapper
@cache
def actual_value(n):
    time.sleep(2)
    return n
# caching program