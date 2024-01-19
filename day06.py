class Animal:
    def says(self):
        return 'I speak'

class Horse(Animal):
    def says(self):
        return 'Neigh'


class Donkey(Animal):
    pass
    # def says(self):
    #     return 'Hee haw'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

m1 = Mule()

print(m1.says())
print(Hinny.__mro__)