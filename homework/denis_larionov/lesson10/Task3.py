
first = int(input('Enter number 1: '))
second = int(input('Enter number 2: '))
action = '-'


def calculated(func):

    def wrapper(first, second, action):
        if first < 0 or second < 0:
            action = '*'
        elif first > second:
            action = '-'
        elif first < second:
            action = '/'
        elif first == second:
            action = '+'
        return func(first, second, action)
    return wrapper


@calculated
def calc(first, second, action):
    if action == '+':
        return first + second
    elif action == '-':
        return first - second
    elif action == '/':
        return first / second
    elif action == '*':
        return first * second


print(calc(int(f'{first}'), int(f'{second}'), action))
