class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')


class Pikachu(Pokemon):
    def __init__(self, name, type):
        super().__init__(name) # 부모 클래스의 init 실행
        self.type =type
    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) {self.type} 공격!')

    def electric_info(self):
        print('전기계열의 공격')

class Squirtl(Pokemon):
    pass

p1 = Pikachu('피카츄', '전기')
p2 = Squirtl('꼬부기')
p1.attack(p2)
p2.attack(p1)
p1.electric_info()