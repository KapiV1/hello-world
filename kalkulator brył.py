import math
PI = math.pi
sqrt2 = math.sqrt(2)
sqrt3 = math.sqrt(3)

print('a - figura na plaszczyznie b - bryla')
inp = input('--- ')
if inp == 'a':
    print('a - Pkwadratu b - Pprostokata c - Pruwnolegloboku d - Ptrapezu e - Ptrukata')
    print('f - Pkola g - Prombu')
    inp = input('--- ')
    if inp == 'a':
        a = float(input('a = '))
        print(f'dla a = {a} pole kwadratu = {a**2} ')
    elif inp == 'b':
        a = float(input('a = '))
        b = float(input('b = '))
        print(f'dla a = {a} i dla b = {b} pole prostokat = {a * b}')
    elif inp == 'c':
        a = float(input('a = '))
        h = float(input('h = '))
        print (f'dla a = {a} i b = {h} pole ruwnolegloboku = {a * h}')
    elif inp == 'd':
        a = float(input('a = '))
        b = float(input('b = '))
        h = float(input('h = '))
        print (f'dla a = {a} i b= {b} i h = {h} pole trapezu = {((a + b) * h)  / 2}')
    elif inp == 'e':
        print('a - Ptrujkat b - PTrujaktaRuwnobocznego')
        inp = input('--- ')
        if inp == 'a':
            a = float(input('a = '))
            h = float(input('h = '))
            print(f'dla a + {a} i h = {h} pole trujkata = { a * h / 2}') 
        elif inp == 'b':
            a = float(input('a = '))
            print(f'dla a = {a} pole trujakta = {(a**sqrt3) / 4}')
    elif inp == 'f':
        r = float(input('r = '))
        print(f'dla r = {r} Pkola = {PI * r**2}')
    elif inp == 'g':
        print('a - ZBokuIWysokosci b - ZPrzekatnych')
        inp = input('--- ')
        if inp == 'a':
            a = float(input('a = '))
            h = float(input('h = '))
            print(f'dla a = {a} i b= {h} pole trapezu = {a * h}')
        elif inp == 'b':
            e = float(input('e = '))
            f = float(input('f = '))
            print(f'dla e = {e} i f = {f} Ptapezu = {(e * f) / 2}')
    else:
        print('coś nietak')  
elif inp == 'b':
    print('a - Objprostopadloscianu b - Objgraniastoslupa c - Objostroslupa')
    print('d - Objstozka e - Objkuli')
    inp = input('--- ')
    if inp == 'a':
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        print(f'dla a = {a} i b = {b} i c = {c} Objprostopadloscianu = {a * b *c}')
    elif inp == 'b':
        Pp = float(input('Pp = '))
        H = float(input('H = '))
        print (f'dla Pp = {Pp} i H = {H} Objgraniastoslupa = {Pp * H}')
    elif inp == 'c':
        Pp = float(input('Pp = '))
        H = float(input('H = '))
        print(f'dla Pp = {Pp} i H = {H} pole ostroslupa = {Pp * H / 3}')
    elif inp == 'd':
        r = float(input('r = '))
        H = float(input('H = '))
        print(f'dla r + {r} i H = {H} Objstozka = {PI * r**2 * H / 3}')
    elif inp == 'e':
        r = float(input('r = '))
        print(f'dla r = {r} Objkuli = {(4 / 3) * PI * r**3}')
else:
    print('coś nietak')
