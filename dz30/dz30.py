class Tower:
    def stay(self):
        return 'stay'


class ArcherTower(Tower):
    def arrow_shot(self):
        return 'arrow shot!'


class CannonTower(Tower):
    def cannon_shot(self):
        return 'cannon shot!'


class MultiTower(CannonTower, ArcherTower):
    def multi_shot(self):
        return 'MULTI SHOT!'


t1 = Tower()
t2 = ArcherTower()
t3 = CannonTower()
t4 = MultiTower()

print(t1.stay())
print(t2.stay(),t2.arrow_shot())
print(t3.stay(),t3.cannon_shot())
print(t4.stay(),t4.cannon_shot(), t4.arrow_shot(), t4.multi_shot())
