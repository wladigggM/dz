class Tower:
    def __init__(self, hp, armor):
        self.__hp = hp
        self.__armor = armor

    def set_armor(self, value):
        self.__armor += value

    def set_hp(self, value):
        self.__hp += value

    @property
    def hp(self):
        return self.__hp

    @property
    def armor(self):
        return self.__armor

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @armor.setter
    def armor(self, value):
        self.__armor = value


class ShootingTower(Tower):
    def __init__(self, hp, armor, dmg):
        super().__init__(hp, armor)
        self.__dmg = dmg

    @property
    def dmg(self):
        return self.__dmg

    def __sub__(self, other):
        print('SHOOT')
        if other.armor > 0:
            return other.armor - self.__dmg
        else:
            return other.hp - self.__dmg


# objects
t1 = Tower(100, 100)
t2 = ShootingTower(100, 80, 10)

while True:
    if t1.armor > 0:
        print(f'hp t1: {t1.hp} armor t1 : {t1.armor}')
        fight = t2 - t1
        t1.armor = fight
        if t1.armor == 0:
            print(f'armor t1: {t1.armor}')

    else:
        if t1.hp > 0:
            print(f'hp t1: {t1.hp} armor t1 : {t1.armor}')
            fight = t2 - t1
            t1.hp = fight
        else:
            print(f'hp t1: {t1.hp}')
            break
