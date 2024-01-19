import random

class OopsException(Exception):
    pass

numbers = [random.randint(0,100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0~{len(numbers)-1}): "))
    print(numbers[pick])
    print(5/2)
    raise OopsException('Oops~') # 강제 예외 발생 C++ 는 throw
except IndexError:
    print("Out of range : wrong index number")
except ValueError:
    print('Input Only Number~')
except OopsException as err:
    print(err)
except Exception as err:
    print(f'Error occurs{err}')
else:
    print(f'program terminate')