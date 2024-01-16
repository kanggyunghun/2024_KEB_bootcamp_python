# prime number 2
number = int(input('enter number :'))
is_prime = True
i = 2

if number < 2:
    print(f'{number}는 prime number가 아닙니다.')
else:
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f'{number}는 prime number 입니다')
    else:
        print(f'{number}는 prime number가 아닙니다.')


