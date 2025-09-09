print('Podaj długości boków trójkąta:') # wprowadzenie
a = float(input('   Podaj długość boku a: '))  # deklaracja zmiennej i pobranie długości boku a
b = float(input('   Podaj długość boku b: '))  # deklaracja zmiennej i pobranie długości boku b
c = float(input('   Podaj długość boku c: '))  # deklaracja zmiennej i pobranie długości boku c
odp = 'Trójkąt o podanych bokach'  # deklaracja zmiennej na końcową odpowiedź i ustawienie początku odpowiedzi

# sprawdzenie czy dane poprawne
if a <= 0 or b <= 0 or c <= 0: 
    odp += ' nie istnieje, ponieważ długości boków muszą być liczbami dodatnimi.' 
elif a + b <= c or a + c <= b or b + c <= a:
    odp += ' nie istnieje, ponieważ suma długości dowolnych 2 boków musi być większa od długości pozostałego boku.' 
else: 
    odp += ' jest '
    # z Pitagorasa czy prostokątny, ostrokątny czy rozwartokątny
    if a**2 + b**2 == c**2  or a**2 + c**2 == b**2 or b**2 + c**2 == a**2: 
        odp += 'prostokątny '
    elif a**2 > b**2 + c**2 or a**2 > c**2 + b**2 or b**2 > c**2 + a**2:
        odp += 'rozwartokątny '
    else:
        odp += 'ostrokątny '

    # porównanie długości boków
    if a == b and a == c:
        odp += 'równoboczny.'
    elif a == b or a == c or b == c:
        odp += 'równoramienny.'
    else:
        odp += 'różnoboczny.'

print(odp) # wypisanie zbudowanej odpowiedzi