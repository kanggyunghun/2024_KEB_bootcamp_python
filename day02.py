<<<<<<< HEAD
# (32°F − 32) × 5/9 = 0°C
# (0°C × 9/5) + 32 = 32°F
# fahrenheit = float(input('Enter temperature in Fahrenheit:'))
# print(f'fahrenheit : {fahrenheit}F, Celsius : {round(((fahrenheit-32.0) *5.0/9.0),2)}C')
# print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0) *5.0/9.0):.2f}C')

temperature = ''
while temperature !='3':
    temperature = input('1) Fahrenheit-> Celsius 2) Celsius -> Fahrenheit 3) Quit program :')

    if temperature == '1':
        fahrenheit = int(input('Enter temperature in Fahrenheit:'))
        print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

    elif temperature == '2':
        celsius = int(input('Enter temperature in Celsius:'))
        print(f'celsius : {celsius}F, Celsius : {((celsius * 9.0/5.0) + 32.0):.4f}F')

    else:
        temperature = '3'
        print('end program')
