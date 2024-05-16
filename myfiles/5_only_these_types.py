def only_these_types(*types):
    def middle(func):
        def wrapper(*args, **kwargs):
            selects = []
            for arg in args:
                for type in types:
                    if isinstance(arg, type):
                        selects.append(arg)
            return func(*selects)
        return wrapper
    return middle
    
@only_these_types(int, float)
def mysum(*numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total

print(mysum(2,3.,6,7.,'boo'))
