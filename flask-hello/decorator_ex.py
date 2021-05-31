import time
curr_time = time.time()

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_func():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_func():
    for i in range(100000000):
        i * i

fast_func()
slow_func()