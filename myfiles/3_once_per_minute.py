import random, time

def one_per_ten(func):
    last_run = None
    def wrapper(*args, **kwargs):
        nonlocal last_run
        now = time.time()
        if last_run and (now - last_run < 10*1000.):
            raise RuntimeError(now - last_run)
        last_run = now
        return func(*args, **kwargs)
    return wrapper
    
@one_per_ten
def slow_add(a, b):
    time.sleep(random.randint(0, 3))
    return a + b

print(slow_add(2, 3))   
print(slow_add(4, 5))  
