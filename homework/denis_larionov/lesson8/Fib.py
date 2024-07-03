def fibonachi():
    fib1 = 0
    fib2 = 1
    i = 0
    n = 3
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield (fib2)
        i += 1
        n += 1


count = 2
for i in fibonachi():
    if count == 5:
        print(i)
        print('=' * 20)
    elif count == 200:
        print(i)
        print('=' * 20)
    elif count == 1000:
        print(i)
        print('=' * 20)
    elif count == 10000:
        print(i)
        print('=' * 20)
        break
    count += 1
