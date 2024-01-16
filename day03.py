# prime number

number = int(input('enter number :'))
count = 0
i = 2

while i <= number:
    if number % i == 0:
        count = count + 1
        break
    i = i + 1

if count == 0:
    print(f'{number}는 prime number 입니다')
else:
    print(f'{number}는 prime number가 아닙니다.')

