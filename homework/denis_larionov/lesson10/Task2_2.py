def repeat(count):


    def funk_repeat(funk):


        def wrapper(*args):
            for i in range(count):
                result = funk(*args)
        return wrapper
    return funk_repeat


@repeat(5)
def hop_and_bob(text):
    print(text)


hop_and_bob('Hi')
