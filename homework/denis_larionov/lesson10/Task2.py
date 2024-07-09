def repeat(func):


    def wrapper(*args, **kwargs):
        count = (int(kwargs['count']))
        for i in range(count):
            result = func(*args)
        return result
    return wrapper


@repeat
def hop_and_bob(text):
    print(text)


hop_and_bob('Hi', count = 5)
