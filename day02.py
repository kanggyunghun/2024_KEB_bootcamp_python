# (32°F − 32) × 5/9 = 0°C
# (0°C × 9/5) + 32 = 32°F
fahrenheit = float(input('Enter temperature in Fahrenheit:'))
print(f'fahrenheit : {fahrenheit}F, Celsius : {round(((fahrenheit-32.0) *5.0/9.0),2)}C')
print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0) *5.0/9.0):.2f}C')

menu = input('1) Fehrenheit -> Celsius 2) Celsius -> Fehrenheit 3) Quit program :')

if menu == '1':
    fahrenheit = float(input('Enter temperature in Fahrenheit:'))
    print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.2f}C')
elif menu == '2':
    celsius = float(input('Enter temperature in Celsius :'))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9/5) + 32):.2f}')
