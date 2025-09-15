print('Podaj długości boków trójkąta:') 
a = float(input('   Podaj długość boku a: '))  # podanie długości boku a
b = float(input('   Podaj długość boku b: '))  # podanie długości boku b
c = float(input('   Podaj długość boku c: '))  # podanie długości boku c
odp = 'Trójkąt o podanych bokach'  

# sprawdzenie czy trujkąt jest możliwy
if  a <= 0 or b <= 0 or c <= 0: 
    odp += ' nie istnieje.' 
elif a + b <= c or a + c <= b or b + c <= a:
    odp += ' nie istnieje.' 
else: 
    odp += ' jest '
    # sprawdzeie czy trujkąt jest: prostokątny, rozwartokątny lub ostrokątny
    if a**2 + b**2 == c**2  or a**2 + c**2 == b**2 or b**2 + c**2 == a**2: 
        odp += 'prostokątny '
    elif a**2 > b**2 + c**2 or a**2 > c**2 + b**2 or b**2 > c**2 + a**2:
        odp += 'rozwartokątny '
    else:
        odp += 'ostrokątny '

    # sprawdzeie czy trujkąt jest: równoboczny, równoramienny lub różnoboczny
    if a == b and a == c:
        odp += 'równoboczny.'
    elif a == b or a == c or b == c:
        odp += 'równoramienny.'
    else:
        odp += 'różnoboczny.'

print(odp) # wypisanie odpowiedzi