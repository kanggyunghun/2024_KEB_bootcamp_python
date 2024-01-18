def is_prime(num) -> bool: # help() 와 같이 사용
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param num: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if num < 2:
        return False
    else:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

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
        if is_prime(num):
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
            if is_prime(num):
                print(num, end =' ')

