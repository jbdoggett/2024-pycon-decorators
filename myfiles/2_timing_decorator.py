import random, time

def timefunc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        with open('timing.txt', mode='a') as file:
            file.write(f'{func.__name__} - {start} - {elapsed_time}\n')
        return result
    return wrapper
    
@timefunc
def slow_add(a, b):
    time.sleep(random.randint(0, 3))
    return a + b

@timefunc
def slow_mul(a, b):
    time.sleep(random.randint(0, 3))
    return a * b

print(slow_add(2, 3))    
print(slow_mul(4, 5))
