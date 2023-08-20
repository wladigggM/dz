class Wallet:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def __add__(self, other):
        print('     __add__')
        if isinstance(other, (int, float)):
            return Wallet(self._balance + other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Wallet(self._balance - other)

    def __eq__(self, other):
        print('     __eq__')
        if self._balance == other._balance:
            return True
        else:
            return False

    def __gt__(self, other):
        print('     __gt__')
        if self._balance > 0:
            return 'Balance > 0'


n = 10

wallet1 = Wallet(1000)
wallet2 = Wallet(2000)

print(wallet1 > 0)
print(wallet1 == wallet2)

wallet1 = wallet1 + n
print(wallet1.balance)

wallet2 = wallet2 - n
print(wallet2.balance)
