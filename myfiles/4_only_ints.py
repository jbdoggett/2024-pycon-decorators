def only_ints(func):
    def wrapper(*args, **kwargs):
        return func(*[i for i in args if isinstance(i, int)])
    return wrapper
    
@only_ints
def mysum(*numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total

print(mysum(2,3.,6,7.,'boo'))
