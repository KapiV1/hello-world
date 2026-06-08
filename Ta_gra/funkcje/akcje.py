from .twoja_postać import Twoja_postać
from .przeciwnicy import moby
from .przeciwnicy import kłody
from random import randint
import time

print(Twoja_postać)

import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def odliczanie():
    print('3')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('1')
    time.sleep(0.5)
    print('GO!')
    time.sleep(0.5)
    clear()


def twój_atak(Twoja_postać, moby, x):
    print(f'hp[{moby[x].życie}] -{Twoja_postać[1]}')
    moby[x].życie -= Twoja_postać[1]


def atak_moba(Twoja_postać, moby, x):
    print(f'hp[{Twoja_postać[0]}] -{moby[x].atak}')
    Twoja_postać[0] -= moby[x].atak

def twój_super_atak(Twoja_postać, moby, x):

    print(f'mana[{Twoja_postać[3]}] -5')
    Twoja_postać[3] -= 5
    odliczanie()
    l = 0
    while l < 4:
            
            r = randint(1, 4)
            if r == 1:
                awds = 'a'
            elif r == 2:
                awds = 'w'
            elif r == 3:
                awds = 'd'
            elif r == 4:
                awds = 's'
            print(awds.upper())
            
            start = time.perf_counter()
            inp = input()
            czas1 = time.perf_counter() - start

            if inp == awds and czas1 <= 1:
                clear()
                l += 1
                
                if l == 4: 
                    print('ATAK KRYTYCZNY!')
                    print(f'hp[{moby[x].życie}] -{Twoja_postać[2]}')                    
                    moby[x].życie -= Twoja_postać[2]
                    break
            
            else:
                l -= 1
                clear()
                
                if l <= 0:
                    print('nieudało się')
                    break

def walka(moby, Twoja_postać):
    l = 0
    while l < 1:
        print('wybierz moba:')
        for i in range(0, len(moby)):
            print(f'{i + 1} - {moby[i].nazwa}')

        inp = input()
        if inp == '1':
            x = 0
            l += 1
            clear()
        elif inp == '2':
            x = 1
            l += 1
            clear()
        else:
            clear()
            print('niema takiego moba')
            print()

    while True:
        i = 0
        while i < 1:
            print()
            print(f'[{moby[x].nazwa}]: hp[{moby[x].życie}] / atak[-{moby[x].atak}]')
            print(f'[TY]: hp[{Twoja_postać[0]}] / a - atak[-{Twoja_postać[1]}] / sa - SUPER ATAK[-{Twoja_postać[2]}] i mana[-5] / mana[{Twoja_postać[3]}]')
            print('(twój róch)')
            inp = input()
            
            if inp == 'a':
                clear()
                twój_atak(Twoja_postać, moby, x)
                i += 1
            
            elif inp == 'sa' and Twoja_postać[3] >= 5:
                clear()
                twój_super_atak(Twoja_postać, moby, x)
                i += 1
            
            else:
                clear()
                print('niema takieho ruchu / masz zamało many')
        
        if moby[x].życie <= 0:
            print()
            print('WYGRAŁEŚ!')
            break

        else:
            print()
            print('róch moba')
            time.sleep(1.5)
            clear()
            atak_moba(Twoja_postać, moby, x)

        if Twoja_postać[0] <= 0:
            print('PRZEGRAŁEŚ!')
            break

def atakój_kłodę(kłody, Twoja_postać, y):
    twoja_siła = Twoja_postać[1] / 2 + Twoja_postać[4]
    odliczanie()
    while kłody[y].odporność > 0:
        r = randint(2, 5)
        r2 = randint(1, 4)
        
        time.sleep(r)

        print(f'{" " * (r2 * 33)} KŁODA')
        
        start = time.perf_counter()
        inp = input()
        czas2 = time.perf_counter() - start
        
        if czas2 <= 0.5 and inp == '':
            kłody[y].odporność -= twoja_siła
            clear()
        else:
            print('za wolno')

def ścinaj_las(kłody, Twoja_postac):
    twoja_siła = Twoja_postać[1] / 2 + Twoja_postać[4]
    print('wybierz kłodę:')

    for i in range(0, len(kłody)):
        print(f'{i + 1} - {kłody[i].nazwa}')

    l = 0
    while l < 1:
        inp = input()
        
        if inp == '1':
            y = 0
            l += 1
        elif inp == '2':
            y = 1
            l += 1
        else:
            print('niema takiej kłody')

    clear()
    print(f'[{kłody[y].nazwa}]: odporność[{kłody[y].odporność}]')
    print(f'[TY]: siła[{twoja_siła}]')
    print('ENTER aby kontynułować')
    inp = input()

    atakój_kłodę(kłody, Twoja_postać, y)





