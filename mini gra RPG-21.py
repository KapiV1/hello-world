from random import randint
import time
import os

#              hp/atack/defence/wydajność/poziom kopalni/odblokowane biomy
TwojaPostać = [10,10,   10,     10,       1,             3]

# listy do walki:
#------------------------------------------------

#                             atack/czy masz(0 - masz)/cena
EqW = [['goła pięść',         0,    0,                 0   ],
       ['drewniany nóż',      10,   1,                 5   ],
       ['żelazny nóż',        17,   1,                 10  ],
       ['żelazny miecz',      30,   1,                 35  ],
       ['diamentowy miecz',   45,   1,                 70  ],
       ['netherytowy miecz',  60,   1,                 120 ],
       ['mace',               120,  1,                 350 ],
       ['orbital strke canon',200,  1,                 1000]
      ]
#                            defence/czy masz(0 - masz)/cena
Zb = [['zkurzana zbroja',    15,     0,                 30 ],
      ['żelazna zbroja',     40,     1,                 55 ],
      ['diamentowa zbroja',  70,     1,                 100],
      ['netheritowa zbroja', 150,    1,                 300]
     ]

#                                   hp/atack/defence/biom/zarobek/żywotność smoka(0 - żyje)
Przeciwnicy  = [['Zombie',          5,  11,   2,     0,   3,     0],
                ['Slime',           20, 17,   5,     0,   10,    0],
                ['witchka',         35, 30,   6,     0,   4,     0],
                # bagno
                
                ['Spider',          5,  11,   3,     1,   5,     0],
                ['skelton',         15, 25,  10,     1,   5,     0],
                ['Posuch',          20, 30,   7,     1,   3,     0],
                ['enderman',        45, 40,  20,     1,   30,    0],
                # pustynia
                
                ['zombie drowner',  20, 30,  10,     2,   3,     0],
                ['guardian',        70, 15,  40,     2,   10,    0],
                ['ocean guardian',  100,30,  75,     2,   15,    0],
                # ocean
                
                ['shulker',         50, 5,   45,     3,   40 ,   0],
                ['endrman grupe',   45, 75,  40,     3,   300,   0],
                ['ender dragon',    150,159, 50  ,     3,   0  , 0]
                # end
              ]

# ogólny: hp/atack/defence           
Ty = [    0, 0,    0]
#------------------------------------------------
# listy do kopania:
#-----------------------------------------------------------------

#                                szczęście/czego/       koszt rudy/koszt uleprzenia krty dostępu
PozK = [['1. poziom - węgiel',   0,       'węgla',      1,         0   ],
        ['2. poziom - żelazo',   0,       'żelaza',     2,         100 ],
        ['3. poziom - lapis',    2,       'lapisu',     5,         300 ],
        ['4. poziom - redstone', 3,       'redstona',  10,         800 ],
        ['5. poziom - diamenty', 0,       'diamentów', 30,         1500]
       ]

#                              wydajność/szczęście/czy masz(0 - masz)/cena
EqK = [['goła pięść',          1,        0,        0,                 0   ],
       ['drwniany kilof',      3,        1,        1,                 7   ],
       ['kamienny kilof',      6,        1,        1,                 15  ],
       ['żelazny kilof',       10,       1,        1,                 50  ],
       ['diamentowy kilof',    17,       2,        1,                 100 ],
       ['netheritowy kilof',   20,       3,        1,                 300 ],
       ['(nieskończoność) TNT',60,       0,        1,                 1000]
      ]
#    Wę  Że  La  Re  Di
M = [0,  0,  0,  0,  0]
# ogólne: wydajność/szczęście
OWS = [   0,        0]
#-----------------------------------------------------------------
# listy do kasyna
#-----------------------------------------------------------------

Re = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
Bl = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
Gr = [0]
#-----------------------------------------------------------------

Pieniądze = 0
# gra

while True:
    
    # waruki zwycięsta
    if Przeciwnicy[12][6] == 1:
        print('Zwyciężyłeś porzez zabicie smoka!!!')
        break
    elif Pieniądze >= 10000:
        print('Zwyciężyłeś porzesz zarobiene 10000 pieniędzy!!!')
        break
    else:
    
        print(f'posiadasz: {Pieniądze} pieniędzy')
        print()
        print('Co robisz?')
        print()
        print('a - idę walczyć')
        print('b - idę kopać')
        print('c - idę do mista handlarzy')
        print()
        print('d - (jak ukończyć grę)')



        inp = input()
        p = ord(inp[0]) - 97 # 'a' daje 0 'b' daje 1 i liczy się tylko pierwszy znak inp
        if p == 0:
            
                # Wybieranie gdzie idziesz
            print('a - bagno')
            print('b - pusynia')
            print('c - ocean')
            print('d - end')
            
            inp = input()
            w = ord(inp[0]) - 97
            print(w)
            if w <= TwojaPostać[5]:
            
            
                # Wybieranie przeciwniaka
                a = 0
                while a < 1:
                    for i in range (0, len(Przeciwnicy)):
                        if Przeciwnicy[i][4] == w:
                            print(f'zawalcz z : {chr(97 + i)} - ({Przeciwnicy[i][0]} / hp: {Przeciwnicy[i][1]} / atack: {Przeciwnicy[i][2]} / defence: {Przeciwnicy[i][3]})')
                            
                    inp = input()
                    Ap = ord(inp[0]) - 97 
                    if Przeciwnicy[Ap][4] == w:
                        Ap = ord(inp[0]) - 97
                        print(f'Wybrałeś : {Przeciwnicy[Ap][0]}')
                        AP = [Przeciwnicy[Ap][1], Przeciwnicy[Ap][2], Przeciwnicy[Ap][3], Przeciwnicy[Ap][5], Przeciwnicy[Ap][6]] #AP - aktualny przeciwnik
                        print('_________')
                        print()
                        a += 1
                    else:
                        print('niema takiego moba')
                
                # Wybierania broni
                h = 0
                while h < 1:
                    for i in range (0, len(EqW)):
                        if EqW[i][2] == 0:
                            print(f'wybierz broń : {chr(97 + i)} - ({EqW[i][0]} / atack: {EqW[i][1]} ) ')
                            
                    inp = input()
                    Ab = ord(inp[0]) - 97
                    if EqW[Ab][2] == 0:
                        print(f'Wybrałeś : {EqW[Ab][0]}')
                        AB = EqW[Ab]                      #AB - aktualna broń
                        print('_________')
                        print()
                        h += 1
                    else:
                        print('nieposiadasz takiej broni')
                    
                # Wybieranie zbroi
                r = 0
                while r < 1:
                    for i in range(0, len(Zb)):
                        if Zb[i][2] == 0:
                            print(f'wybierz zbroję : {chr(97 + i)} - ({Zb[i][0]}) / defence({Zb[i][1]})')
                    
                    inp = input()
                    Az = ord(inp[0]) - 97
                    if Zb[Az][2] == 0:
                        print(f'wybrałeś : {Zb[Az][0]}')
                        AZ = Zb[Az]                     # AZ - aktualna zbroja
                        print('_________')
                        print()
                        r += 1
                    else:
                        print('niemasz takiej zbroji')
                    AhpTP = TwojaPostać[0]   #AhpTP - aktualne hp twojej postaci

                # Wejście do walki
                inp = input('ENTER aby zacząć walkę!!!')
                os.system('cls')
                print('_________')
                print()
                if inp == (''):
                    Ty[0] = TwojaPostać[0]
                    Ty[1] = TwojaPostać[1] + AB[1]
                    Ty[2] = TwojaPostać[2] + AZ[1]
                    print('Twoje parametry:')
                    print(f'( hp: {Ty[0]} / atack: {Ty[1]} / defence: {Ty[2]})')
                    print()
                    print('Parametry przeciwnika')
                    print(f'( hp: {AP[0]} / atack: {AP[1]} / defence: {AP[2]})')

                    # Walka
                    while True:
                        print('_________')
                        print()
                        inp = input('ENTER aby ZAATAKOWAĆ!!!')
                        print('_________')
                        print()
                        AP[0] -= max((Ty[1] - AP[2]), 0) # zmniejszam hp przeciwnika o różnicę między moim atakiem a jego obroną, chyba że jego obrona jest większa niż mój atak
                        if AP[0] <= 0:
                            os.system('cls')
                            Przeciwnicy[Ap][6] = 1
                            print(f'zwyciężłeś z {Przeciwnicy[Ap][0]}')
                            print(f'po sprzedaży łupu z moba otrzymałeś {AP[3]} pieniędzy')
                            Pieniądze += AP[3]

                            print()
                            break
                        
                        print(f'hp przeciwnika - ({AP[0]})')
                        print()
                        print('PRZECIWNIK CIĘ ATAKUJE')
                        print()
                        time.sleep(2.5)
                        
                        Ty[0] -= max((AP[1] - Ty[2]), 0)
                        if Ty[0] <= 0:
                            os.system('cls')
                            print(f'przegrałeś z {Przeciwnicy[Ap][0]}')
                            print()
                            break
                        print(f'twoje hp - ({Ty[0]})')
            else:
                print('niewiesz gdzie to jest')
                print('(musisz najpierw kupić kawałek mapy u kartografa)')
                print('_____________________________________')
                print()
        
        # kopanie
        elif p == 1:
            os.system('cls')
            
            if Pieniądze >= 10: 
                print('WITAJ w kopalni!')
                print('wpłać 10 pieniążków aby wejść dalej')
                inp = input('ENTER aby wpłacić 10 pieniążków')
                print('_____________________________________')
                print()
                print(f'Masz dostęp do: {TwojaPostać[4]} poziomów kopalni')
                
                for i in range(0, TwojaPostać[4]):
                    print ()
                inp = input('wpisz poziom kopalni, aby do niego zjechać: ')
                WybPoz = ord(inp[0]) - 49 # '1' => 0...
                
                if WybPoz <= TwojaPostać[4] - 1:
                    Pieniądze -= 10
                    print(f'witaj na {WybPoz + 1} poziomie')
                    print('czm chcesz kopać')
                    
                    for a in range(0, len(EqK)):
                        if EqK[a][3] == 0:
                            print(f'wybierz narzędzie : {chr(97 + a)} - ({EqK[a][0]} / wydajność: {EqK[a][1]} / szczęście: {EqK[a][2]} ) ')                                    
                    inp = input()
                    An = ord(inp[0]) - 97
                    
                    if An >= len(EqK): # wybrana litera nie istnieje w ekwipunku
                        print('wybrana litera nie istnieje w ekwipunku') 
                        An = 0                    
                    elif EqK[An][3] == 1: # nie masz dostępu do tego ekwipunku
                        print('nie masz dostępu do tego ekwipunku')
                        An = 0
                    
                    print(f'wybrałeś - {EqK[An][0]}')
                    OWS[0] = EqK[An][1]
                    OWS[1] = EqK[An][2]
                    sekKop = 1
                    
                    while sekKop > 0:
                        print(f'wpisz ile sekund chcesz kopać (1s = {OWS[0]} {PozK[WybPoz][2]}.)')
                        print(f'1 {PozK[WybPoz][2]} - zarobek pieniążków:  {PozK[WybPoz][3]}.')
                        sekKop = int(input()) # możnaby dodać jakąś idiotooporność.
                        
                        for i in range(0, sekKop):
                            M[WybPoz] += OWS[0]
                            x = OWS[1]        # x - drop z szczęścia
                            n = randint(0, 10)
                            if x >= n:
                                M[WybPoz] += OWS[0]
                            print(f'aktualny stan {PozK[WybPoz][2]} - {M[WybPoz]}')
                            time.sleep(1)
                        os.system('cls')
                        print(f'wykopałeś {M[WybPoz]} {PozK[WybPoz][2]}')
                        Pieniądze += M[WybPoz] * PozK[WybPoz][3]
                        print()
                        print('_____________________________________')
                        print()
                else:
                    print('niemasz dostępu do tego poziomu kopalni')
                    print('(musisz go uleprzyć u górnika)')
                    print('_____________________________________')
                    print()
            else:
                print('WYWALAJ STĄD BIEDAKU')
                print('(musisz mieć conajmniej 10 pieniążków)')
        
        # miasto
        elif p == 2:
            print('witaj w mieście handlarzy!!!')
            print('a - idź do sklepu')
            print('b - idź do kartografa')
            #print('c - idź do kasyna')
            print('d - idź do górnika')
            inp = input()
            q = ord(inp[0]) - 97
            if q == 0:
                print('witaj w sklepie')
                print('czego poszukujesz?')
                print('a - bronie')
                print('b - zbroje')
                print('c - kilofy')
                inp = input()
                b = ord(inp[0]) - 97
                if b == 0:
                    for i in range(0, len(EqW) - 1):
                        print('_____________________________________')
                        print()
                        print(f'{chr(i + 97)} - {EqW[i + 1][0]} / atak: {EqW[i + 1][1]} / cena: {EqW[i + 1][3]}')
                    inp = input()
                    p = ord(inp[0]) - 97
                    
                    CWB = EqW[p + 1][3] #CWB - cena wybrnej broni
                    if Pieniądze < CWB:
                        print('niestać cię')
                    else:
                        Pieniądze -= CWB
                        EqW[p + 1][2] = 0
                        print(f'diękuje za zakup')
                        print(f'otrzymałeś ({EqW[p + 1][0]})')
                        print('_____________________________________')
                        print()
                elif b == 1:
                    for i in range(0, len(Zb)):
                        print('_____________________________________')
                        print()
                        print(f'{chr(i + 97)} - {Zb[i][0]} / atak: {Zb[i][1]} / cena: {Zb[i][3]}')
                    inp = input()
                    p = ord(inp[0]) - 97

                    CWZ = Zb[p][3] #CWZ - cena wybranej zbroi
                    if Pieniądze < CWZ:
                        print('niestać cię')
                    else:
                        Pieniądze -= CWZ
                        Zb[p][2] = 0
                        print('dziękuje za zakup ')
                        print(f'otrzymałeś ({Zb[p][0]})')
                        print('_____________________________________')
                        print()
                elif b == 2:
                    for i in range(0, len(EqK) - 1):
                        print('_____________________________________')
                        print()
                        print(f'{chr(i + 97)} - {EqK[i + 1][0]} / wydajność: {EqK[i + 1][1]} / szczęście: {EqK[i + 1][2]} / cena: {EqK[i + 1][4]}')
                    inp = input()
                    p = ord(inp[0]) - 97

                    CWK = EqK[p][4] # CWK - cena wybranego kilofa
                    if Pieniądze < CWK:
                        print('niestać cię')
                    else:
                        Pieniądze -= CWK
                        EqK[p][3] = 0
                        print('dziękuje za zakup ')
                        print(f'otrzymałeś ({EqK[p][0]})')
                        print('_____________________________________')
                        print()
            elif q == 1:
                print('Witaj podruzniku')
                print('zapewne szukasz kawałków mapy')
                print('oto one:')
                
                print('a - 1. kawałek mapy / cena: 300')
                print('b - 2. kawałek mapy / cena: 800')
                print('c - 3. kawałek mapy / cena: 1400')

                inp = input()
                p = ord(inp[0]) - 97
                if p == 0:
                    if Pieniądze >= 300:
                        print('dziękuje za zakup 1. kawałka mapy')
                        Pieniądze -= 300
                        TwojaPostać[5] = 1
                    else:
                        print('niemasz tyle pieniędzy')

                elif p == 1 and TwojaPostać[5] == 1:
                    if Pieniądze >= 800:
                        print('dziękuje za zakup 2. kawałka mapy')
                        Pieniądze -= 800
                        TwojaPostać[5] = 2
                    else:
                        print('niemasz tyle pieniędzy')

                elif p == 2 and TwojaPostać[5] == 2:
                    if Pieniądze >= 1400:
                        print('dziękuje za zakup 3. kawałka mapy')
                        Pieniądze -= 1400
                        TwojaPostać[5] = 3
                    else:
                        print('niemasz tyle pieniędzy')

                else:
                    print('niema takiego kawałka mapy, lub niemasz do niego dostepu')
                    print('(kawałki mapy nusisz kupować pokolei)')

            # elif q == 2:

            #     print('a - ruletka')
                
            #     inp = input()
            #     p = ord(inp[0]) - 97
            #     if p == 0:
            #         j = 0
            #         while j == 0:
            #             print('obstaw dowolny kolor:')
            #             print(f'a - czerwone / {Re}')
            #             print(f'b - czarne / {Bl}')
            #             print(f'z - zielone / {Gr}')
            #             c = input()
            #             p = ord(inp[0]) - 97
            #             if c == 1 or c == 2 or c == 3:
            #                 j = 1
            #                 print('obstaw pieniądze:')
            #                 v = input()
            #                 if v <= Pieniądze:
            #                     for 

            #                     print(f'twój kolor - {}')
                        
            #             else:
            #                 print('niema takiej liczby')
                            

            #                 print('ENTER ayb wylosować')
            #                 inp = input()
            #                 Rl = randint(0, 36) #Rl - losowa liczba
            elif q == 3:
                print('pewnie chcesz ulepszyć kartę dostępu do kopalni')
                print('ENTER aby ulepszyć kartę dostępu')
                inp = input()
                Ad = TwojaPostać[4] # aktualny dostęp
                KUD = PozK[Ad + 1][4] # KUD koszt ulepszenia dostepu
                if Pieniądze < KUD:
                    print('niestać cie!!!')
                    print('_____________________________________')
                    print()
                else:
                    Pieniądze -= KUD
                    TwojaPostać[4] += 1
                    print('dziękuję za zakup ulepszenia')
                    print(f'aktualny pozim karty górniczej {TwojaPostać[4]}')
                    print('_____________________________________')
                    print()




        elif p == 3:
            print('WARUNKI UKOŃCZENIA GRY:')
            print('musisz:')
            print('zabić smoka endu')
            print('lub zarobić 10000 pieniędzy')
            print('_____________________________________')
            print()