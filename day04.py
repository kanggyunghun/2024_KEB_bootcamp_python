while True:
    menu = input('1) Fahrenheit-> Celsius 2) Celsius -> Fahrenheit 3) Prime1 4) Prime2 5) Quit :')

    if menu == '1':
        fahrenheit = int(input('Enter temperature in Fahrenheit:'))
        print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

    elif menu == '2':
        celsius = int(input('Enter temperature in Celsius:'))
        print(f'celsius : {celsius}F, Celsius : {((celsius * 9.0/5.0) + 32.0):.4f}F')

    elif menu == '3':
        number = int(input('enter number :'))
        is_prime = True

        if number < 2:
            print(f'{number}는 prime number가 아닙니다.')
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
                i += 1

            if is_prime:
                print(f'{number}는 prime number 입니다')
            else:
                print(f'{number}는 prime number가 아닙니다.')

    elif menu == '4':
        numbers = input('enter number :').split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')

    elif menu == '5':
        pass

    else:
        print('invalid Menu')


