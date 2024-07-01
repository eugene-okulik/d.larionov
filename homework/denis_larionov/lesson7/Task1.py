def ugadayka():
    while True:
        x = int(2)
        y = int(input('Enter number: '))
        if y == x:
            print('You win!')
            break
        else:
            print('Please enter number again!')
            continue
    print('You cool!')


ugadayka()
