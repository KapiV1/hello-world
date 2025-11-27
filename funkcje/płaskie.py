import math
PI = math.pi



def P_kwadratu(a:float)->float:
    return a**2

def Obw_kwadratu(a:float)->float:
    return a * 4

def P_trujkąta_równobocznego(a, h:float)->float:
    return a * h / 2

def Obw_trójkąta(a:float)->float:
    a * 3

def P_koła(r:float)->float:
    return PI * r**2

def Obw_koła(r:float)->float:
    return 2 * PI * r

def P_prostoąka(a, b:float)->float:
    return a * b

def Obw_prostokąta(a, b:float)->float:
    return a * 2 + b * 2

def P_trapezu(a, b, h:float)->float:
    return (a + b) * h / 2

def Obw_trapezu(a, b, c, d:float)->float:
    return a + b + c + d

def wzory_płaskie()->None:
    while True:
        
        print('a - P_kwadratu b - Obw_kwadratu   c - P_trójkąta d - Obw_trójkąt   f - P_koła g - Obw_kłoa   h - P_prostokąta i - Obw_prostokąta   j - P_trapezu   k - Obw_trapezu e - exit')
        inp:str = input(': ')
        if inp == 'a':
            a:float = float(input('a: '))
            print(f'P_kwadratu = {P_kwadratu(a)}')
        elif inp == 'b':
            a:float = float(input('a: '))
            print(f'Obw_kwadratu = {Obw_kwadratu(a)}')
        elif inp == 'c':
            a:float = float(input('a: '))
            h:float = float(input('h: '))
            print(f'P_trujkąta_równobocznego = {P_trujkąta_równobocznego(a, h)}')
        elif inp == 'd':
            a:float = float(input('a: '))
            print(f'Obw_trójkąta = {Obw_trójkąta(a)}')
        elif inp == 'f':
            r:float = float(input('r: '))
            print(f'P_koła = {P_koła(r)}')
        elif inp == 'g':
            r:float = float(Obw_koła('r: '))
            print(f'Obw_koła = {Obw_koła(r)}')
        elif inp == 'h':
            a:float = float(input('a: '))
            b:float = float(input('b: '))
            print(P_prostokąta = {P_prostoąka(a, b)})
        elif inp == 'i':
            a:float = float(input('a: '))
            b:float = float(input('b: '))
            print(f'Obw_prostokąta = {Obw_prostokąta(a, b)}')
        elif inp == 'j':
            a:float = float(input('a: '))
            b:float = float(input('b: '))
            h:float = float(input('h: '))
            print(f'P_trapezu = {P_trapezu(a, b, h)}')
        elif inp == 'k':
            a:float = float(input('a: '))
            b:float = float(input('b: '))
            c:float = float(input('c: '))
            d:float = float(input('d: '))
            print(f'Obw_trapezu = {Obw_trapezu(a, b, c, d)}')
        elif inp == 'e':
            break


