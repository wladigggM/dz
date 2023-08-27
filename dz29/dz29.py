"""
Создать класс Person, который содержит:

переменные fullName, age - должны быть закрыты;
методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит".
создайте геттеры и сеттеры для закрытых полей класса
Создайте два объекта этого класса.
Вызовите методы move() и talk().

"""


class Person:
    def __init__(self, fullName: str = None, age: int = None):
        self._fullName = fullName
        self._age = age

    @property
    def fullName(self):
        return self._fullName

    def set_fullName(self, value:str):
        self._fullName = value

    @property
    def age(self):
        return self._age

    def set_age(self, value:int):
        self._age = value

    def move(self):
        return f'Полное имя: {self.fullName} Возраст: {self.age}\nдвигается\n'

    def talk(self):
        return f'Полное имя: {self.fullName} Возраст: {self.age}\nговорит\n'


p = Person('Олег Олегович', 43)
p2 = Person('Станислав Станиславович', 35)

print(p.move())
p.set_age(10)
print(p.talk())

print(p2.move())
p2.set_fullName('Алексей Алексеевич')
print(p2.talk())
