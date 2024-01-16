menu = ''

while menu !='5':
    menu = input('\n1) Fahrenheit-> Celsius \n2) Celsius -> Fahrenheit \n3) Detect prime number \n4) Detect prime number between \n5) END'
                   '\nEnter number : ')

    if menu == '1':
        fahrenheit = int(input('Enter temperature in Fahrenheit:'))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

    elif menu == '2':
        celsius = int(input('Enter temperature in Celsius:'))
        print(f'celsius : {celsius}F, Celsius : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')

    elif menu == '3':
        num = int(input('Enter number: '))
        i = 2

        if num < 2:
            pass

        while i < num:
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
                i = i + 1
        if is_prime:
            print(f'{num} is a prime number')
        else:
            print(f'{num} is not a prime number')

    elif menu == '4':
        num = input('Enter two numbers: ').split()
        n1 = int(num[0])
        n2 = int(num[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for num in range(n1, n2+1):
            if num < 2:
                pass

            for i in range(2,num):
                if num % i == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True

            if is_prime:
                print(f'{num}', end = " ")

    elif menu == '5':
        print('End program')

    else:
        print('Menu 중에서 선택해 주세요!')







