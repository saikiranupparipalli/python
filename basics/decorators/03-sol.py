def greet(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)  
        loop_arg =  ", ".join(str(arg) for arg in args)
        loop_kwarg = ", ".join(f"{k}:{v}" for k,v in kwargs.items())
        print(f"{func.__name__} has greeted {loop_arg}")
        print(f"{func.__name__} has greeted {args}")
        print(f"{func.__name__} has greeted {kwargs}")
        print(f"{func.__name__} has greeted {loop_kwarg}")
        
        return func(*args, **kwargs)
    return wrapper

@greet
def greetings(name = 'kiran', msg = 'Hello, '):
    # print()
    return f"{msg} {name}"
greetings(name='sai', msg='namaste')