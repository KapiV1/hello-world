import pygame
from FNAF_rpg import A1
from FNAF_rpg import A2

LIGHT_GREY = (195, 195, 195)
WHITE = (255, 255,255)

x = 1400
y = 800


        
pygame.font.init()
pygame.mixer.init()



door_close_sound = pygame.mixer.Sound(r"C:\Users\kacpe\OneDrive\Pulpit\VSCode\pygame\ound_FNAF\violent-door-slam-395764.mp3")
#door_close_sound2 = door_close_sound.set_volume(0.5)

cam_sound = pygame.mixer.Sound(r"C:\Users\kacpe\OneDrive\Pulpit\VSCode\pygame\ound_FNAF\camera-blip-395761.mp3")

A2_sound = pygame.mixer.Sound(r"C:\Users\kacpe\OneDrive\Pulpit\VSCode\pygame\ound_FNAF\t3-footstep-sfx-323056.mp3") #ch(0)


my_font = pygame.font.Font("Digital-7.ttf", 60)


batria = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\ateria.png')
batria = pygame.transform.scale(batria, (470, 200))

screen = pygame.display.set_mode((x, y))

biuro = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\office.1.jpg')
biuro2 = pygame.transform.scale(biuro, (1400, 800))


door2 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\rzut_ekranu_2025-12-15_110240-removebg-preview.png')
door2 = pygame.transform.scale(door2, (300, 810))
door2_warunki = [0]

door1 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\ore1.png')
door1_warunki = [0]


cam_sys = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\cam.sytem1.png')
cam_sys2 = pygame.transform.scale(cam_sys, (1400, 850))
cam_sys_warunki = [0, 0]

cam1_hitbox = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\cam1_hitbox.png')
cam1_hitbox2 = pygame.transform.scale(cam1_hitbox, (150, 80))
cam1 = [0]

cam2_hitbox = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\cam2_hitbox.png')
cam2_hitbox2 = pygame.transform.scale(cam2_hitbox, (150, 80))
cam2 = [0]


a3 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\a3.png')
a3 = pygame.transform.scale(a3, (450, 240))
a3pos = [[-1000, -1000], [290, 245], [370, 215], [530, 320], [-1000, -1000]]
def rysuj_a3(screen, A):
    screen.blit(a3, a3pos[A[0]])


def zamykanie_pierwszyzh_drzwi(stan_baterii,):
    door1_warunki[0] = 1 - door1_warunki[0]
    if stan_baterii <= 0:
        door1_warunki[0] = 0

def zamykanie_drugich_drzwi(stan_baterii):    
    door2_warunki[0] = 1 - door2_warunki[0]
    if stan_baterii <= 0:
        door2_warunki[0] = 0

def otw_zamk_kam(stan_baterii):
    cam_sys_warunki[0] = 1 - cam_sys_warunki[0]
    if stan_baterii <= 0:
        cam_sys_warunki[0] = 0
    if cam_sys_warunki[0] == 0: zamknij_cam()

def wez_door():
    return [door1_warunki[0], door2_warunki[0], 1]

def otworz_cam1():
    cam1[0] = 1 


def otworz_cam2():
    cam2[0] = 1 

def zamknij_cam():
    cam1[0] = 0
    cam2[0] = 0


def wez_cam_sys():
    return cam_sys_warunki[0] 

pygame.mixer.Channel(2).set_volume(0.35)
sound_started = [0, 0, 0, 0, 0, 0, 0, 0]

def pov_biura(Animy, procent_baterii, hour):
    
     
    screen.blit(biuro2, (0, 0))

    if door1_warunki[0] == 1:
        screen.blit(door1, (-150, 100))
        
        if sound_started[3] == 0:
            pygame.mixer.Channel(2).play(door_close_sound)
            sound_started[3] = 1

    else:
        sound_started[3] = 0
    
    if door2_warunki[0] == 1:
        screen.blit(door2, (1025, 20))

        if sound_started[4] == 0:
            pygame.mixer.Channel(2).play(door_close_sound)
            sound_started[4] = 1

    else:
        sound_started[4] = 0

    rysuj_a3(screen, Animy[2])

    if cam_sys_warunki[0] == 1 and (cam1[0] == 0 or cam2[0] == 0):
        screen.blit(cam_sys2, (0, 0))
        screen.blit(cam1_hitbox2, (420, 193))
        screen.blit(cam2_hitbox2, (830, 173))
    if cam1[0] == 1:
        A1.pov_cam1(screen, Animy[0])   
        
        if sound_started[1] == 0:
            pygame.mixer.Channel(1).play(cam_sound)
            sound_started[1] = 1
       
    else:
        sound_started[1] = 0
    
    if cam2[0] == 1:  
        A2.pov_cam2(screen, Animy[1])

        if sound_started[2] == 0:
            pygame.mixer.Channel(1).play(cam_sound)
            sound_started[2] = 1

    else:
        sound_started[2] = 0    
    
    screen.blit(batria, (-50, 675))

    pygame.draw.rect(screen, LIGHT_GREY, (101, 740, procent_baterii, 30), 0)
    text_surface = my_font.render(hour, True, WHITE)
    screen.blit(text_surface, (1300,0))
    pygame.display.flip()
    
    if Animy[1][0] == 1:
        if sound_started[0] == 0: 
            pygame.mixer.Channel(0).play(A2_sound)
            sound_started[0] = 1
    else: 
        sound_started[0] = 0




    