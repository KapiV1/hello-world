kasa = float(input('podaj kasę ')) #Ilość kasy.
wiek = float(input('podaj wiek ')) #Wiek.


#Wyliczenia z wieku w porównaniu do kasy.
if kasa <= 100 or wiek <= 13:
    print('Niema obcji.')
elif kasa <= 2000 or wiek <= 18:
    print('Jeszcze trochę poczekaj.')
elif kasa > 2000 and wiek <= 30:
    print('Jest git.')
elif kasa > 2000 or wiek <= 45:
    print('Już trochę za pużno.')
else:
    print('Dużo za puźno.')