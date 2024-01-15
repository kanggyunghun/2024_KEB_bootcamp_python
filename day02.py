# (32°F − 32) × 5/9 = 0°C
fahrenheit = float(input('Enter temperature in Fahrenheit:'))
print(f'fahrenheit : {fahrenheit}F, Celsius : {round(((fahrenheit-32.0) *5.0/9.0),2)}C')
print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0) *5.0/9.0):.2f}C')