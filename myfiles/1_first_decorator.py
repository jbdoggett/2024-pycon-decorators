def shouter(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs).upper()}!'
    return wrapper
    
@shouter
def go(a):
    return a

for a in ('jesse', 'bartley', 'doggett'):
    print(go(a))
