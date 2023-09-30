class Product:
    def __init__(self, name: str, price: int, types: str):
        if type(name) is not (str):
            raise "name не соответствует типу str"

        self.__price_checker(price)

        if type(types) is not (str):
            raise "types не соответствует типу str"

        self.name = name
        self.__price = price
        self.types = types

    def __price_checker(self, price):

        if not (type(price)) in [float, int]:
            raise "price не соответствует типу int/float"
        if price < 0:
            raise "price меньше нуля"
        return True

    @property
    def price(self):

        return self.__price

    @price.setter
    def price(self, value):
        self.__price_checker(value)
