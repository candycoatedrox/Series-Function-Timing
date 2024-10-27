from time import perf_counter
from functools import wraps

def time_function(func):
    'Decorator that returns the amount of time it took to run a function.'
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        return (t2 - t1), result
    return wrapper