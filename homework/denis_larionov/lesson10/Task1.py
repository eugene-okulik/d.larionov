def hi_bob(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('You Cool, Bob!')
        print(result)
        return result
    return wrapper


@hi_bob
def hop_and_bob(text):
    print(text)


hop_and_bob('Hi, Bob!')
