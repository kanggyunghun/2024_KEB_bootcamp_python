import random

drinks_food = {'위스키':'초콜릿', '와인': '치즈', '소주': '삼겹살', '고량주': '양꼬치'}
japan_drinks_food = {'사케': '벙어', '위스키': '낙곱새'}
drinks_food.update(japan_drinks_food)
drinks_foods_keys = list(drinks_food)
print(drinks_foods_keys)

while True:
    menu = input(f'다음 술중에 고르시오\n1){drinks_foods_keys[0]}, 2){drinks_foods_keys[1]}, 3){drinks_foods_keys[2]}, 4){drinks_foods_keys[3]} 5)random 6)quit :')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_food[drinks_foods_keys[0]]}')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_food[drinks_foods_keys[1]]}')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_food[drinks_foods_keys[2]]}')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_food[drinks_foods_keys[3]]}')
    elif menu == '5':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_food[random_drink]}')
    elif menu == '6':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_food[drinks_foods_keys[4]]}')
    elif menu == '7':
        print(f'see u next time')
        break
