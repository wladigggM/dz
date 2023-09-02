class Animal:
    def __init__(self, name, age: int, breed):
        self.name = name  # открытый атрибут можем использовать где угодно
        self._age = age  # защищенный атрибут может использоваться внутри класса и у наследников
        self.__breed = breed  # приватный атрибут может использоваться только внутри класса

    def exists(self):
        return 'exist'

    @property
    def breed(self):
        return self.__breed


class Dog(Animal):
    def __str__(self):
        self.exists
        # (+ self.__breed) в наследнике не можем использовать этот атрибут по этому берем значение из геттера
        return 'DOG: ' + self.name + f' {self._age} age ' + self.breed


a1 = Dog('Bobik', 7, 'Labrodor')

print('NAME:' + a1.name)
print('AGE: ' + f'{a1._age}')  # можно но не нужно

# print(a1.__breed)  # выдаст ошибку

print(a1)
print(a1.exists())
