import random

# numbers = []
# for i in range(1,101):
#     numbers.append(random.randint(1,100))
numbers = [random.randint(0,100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0~{len(numbers)-1}): "))
    print(numbers[pick])
except IndexError:
    print("Out of range : wrong index number")
except ValueError:
    print('Input Only Number~')
except Exception:
    print('Error occurs')