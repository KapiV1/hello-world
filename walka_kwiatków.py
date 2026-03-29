from random import randint

class Kwiatek:
    def __init__(self, name, damage, crit_damage, hp, life, victory):
        self.name = name
        self.damage = damage
        self.crit_damage = crit_damage
        self.hp = hp
        self.life = life
        self.victory = victory

    def atak(self)->None:
        self.hp -= self.damage
        if self.hp <= 0:
            self.life = 0

    def crit_atak(self)->None:
        self.hp -= self.crit_damage
        if self.hp <= -1:
            self.life = 0
        
    def victory_(self)->None:
        if self.life == 0:
            self.victory = 1
            print('---------------------------')
            print(f'loser: {self.name}')

tulipan = Kwiatek('rurza', 1, 2, 10, 1, 0)
rurza = Kwiatek('tulipan', 1, 2, 10, 1, 0)

print('---------------------------')
print(f'hp - {rurza.name} - {rurza.hp}')
print(f'hp - {tulipan.name} - {tulipan.hp}')

c = randint(1, 2)

while True:
    print('---------------------------')

    if c == 1 or c == 0:
        a = randint(1, 2)
        if a == 1:
            rurza.atak()
            rurza.victory_()
            c = 0
        elif a == 2:
            rurza.crit_atak()
            rurza.victory_()
            c = 0
    
    if rurza.victory == 1 or tulipan.victory == 1:
        break

    print(f'hp - {rurza.name} - {rurza.hp}')
    
    if c == 2 or c == 0:
        b = randint(1, 2)
        if b == 1:
            tulipan.atak()
            tulipan.victory_()
            c = 0
        elif b == 2:
            tulipan.crit_atak()
            tulipan.victory_()
            c = 0

    if rurza.victory == 1 or tulipan.victory == 1:
        break

    print(f'hp - {tulipan.name} - {tulipan.hp}')