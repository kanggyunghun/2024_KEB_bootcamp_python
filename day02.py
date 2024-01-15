base_number = int(input('input base number :'))
exponent_number = int(input('input exponent number :'))

print(f'base {base_number}, exponent {exponent_number}, 결과 값은:{base_number**exponent_number}')
print('base {0}, exponent {1}, 결과 값은:{2}'.format(base_number, exponent_number,base_number**exponent_number))
print('base %d, exponent %d, 결과 값은 %d' % (base_number, exponent_number,base_number**exponent_number))

# money = 5,000,000 # 쉼표는 튜플로 동작한다.
# print(money)
# print(type(money)) # tuple
# cash = 5_000_000
# print(cash, type(cash))
#
