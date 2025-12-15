import pygame as pg
import math
from FNAF_rpg import office
from FNAF_rpg import A1
from random import randint

bang_sound1 = pg.mixer.Sound(r"C:\Users\kacpe\OneDrive\Pulpit\VSCode\pygame\ound_FNAF\ani-big-pipe-hit-6814.mp3")

bang_sound2 = pg.mixer.Sound(r"C:\Users\kacpe\OneDrive\Pulpit\VSCode\pygame\ound_FNAF\metal-whoosh-hit-7-201910.mp3")

clock = pg.time.Clock()

max_tura = 2700
tura = 0

# pole ekranu
x = 1400
y = 800
maxTrudnosc = 20

screen = pg.display.set_mode((x, y))
max_stan_baterii = 5000
stan_baterii = max_stan_baterii
złużycie_baterii = [1, 1, 1, 1]

Animy =[[0, 4, 0, 0],[0, 2, 0, 1],[0, 4, 10, 2]]

def Ruch_Anima (A):
    r = randint(0, 20) 
    if r < A[2]:
        if A[3] == 0 and A[0] == 3 and office.door1_warunki[0] == 1:
            pg.mixer.Channel(3).play(bang_sound1)

        if A[3] == 1 and A[0] == 1 and office.door2_warunki[0] == 1:
            pg.mixer.Channel(3).play(bang_sound2)

        if A[0] == A[1]-1 and office.wez_door()[A[3]] == 1:
            if A[3] != 2 or A[0] != A[1]-1:
                A[0] = 0
        else:
            A[0] += 1
     


# główna pętla
running = True
while running:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
                running = False
                break
        
        
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_a: office.zamykanie_pierwszyzh_drzwi(stan_baterii)
            
            elif event.key == pg.K_d: office.zamykanie_drugich_drzwi(stan_baterii)
            
            elif event.key == pg.K_s: office.otw_zamk_kam(stan_baterii)
                
            
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            print(pos)
            if 420 <= pos[0] <= 570 and 193 <= pos[1] <= 273 and office.wez_cam_sys() == 1:
                print('cam1')
                office.otworz_cam1()

            if 830 <= pos[0] <= 980 and 173 <= pos[1] <= 253 and office.wez_cam_sys() == 1:
                    print('cam2')
                    office.otworz_cam2()

            if 447 <= pos[0] <= 290 + 447 and 357 <= pos[1] <= 357 + 245 and office.wez_cam_sys() == 0 and Animy[2][0] == 1:
                Animy[2][0] = 0
    
            if 524 <= pos[0] <= 370 + 524 and 343 <= pos[1] <= 343 + 215 and office.wez_cam_sys() == 0 and Animy[2][0] == 2:
                Animy[2][0] = 0

            if 685 <= pos[0] <= 685 + 530 and 447 <= pos[1] <= 447 + 320 and office.wez_cam_sys() == 0 and Animy[2][0] == 3:
                Animy[2][0] = 0
    
    stan_baterii -= office.wez_door()[0] * złużycie_baterii[0]
    stan_baterii -= office.wez_door()[1] * złużycie_baterii[1]
    stan_baterii -= office.wez_cam_sys() * złużycie_baterii[2]
    if Animy[2][0] == 3:
        stan_baterii -= złużycie_baterii[3]
    

    if stan_baterii<= 0:
        office.zamykanie_pierwszyzh_drzwi(stan_baterii)
        office.zamykanie_drugich_drzwi(stan_baterii)
        office.otw_zamk_kam(stan_baterii)
    
    #print(stan_baterii)
    
   
    tura += 1
    if math.floor(tura/10) == tura/10:
        for i in range(len(Animy)):
            Ruch_Anima(Animy[i])
    #print(f'{tura} {Animy}')   

    strhour = str(math.floor(6 * tura / max_tura)) + ':00' 
    if strhour == '6:00': 
        running = False
        print('WYGRAŁEŚ')
    office.pov_biura(Animy, int(math.floor(100 * stan_baterii / max_stan_baterii)), strhour)
    for i in range(len(Animy)-1):
        if Animy[i][0] == Animy[i][1]: 
            running = False
            print('PRZEGRAŁEŚ')
    clock.tick(10)
