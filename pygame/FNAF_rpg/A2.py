import pygame

a2pos = [[-1000, -1000], [50, 300], [-1000, -1000]]

cam2 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\cam.2.webp')
a2 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\a.1.2.png')
cam2 = pygame.transform.scale(cam2, (1700, 800))



def pov_cam2(screen, A):
    screen.blit(cam2, (0, 0))
    screen.blit(a2, a2pos[A[0]])
    pygame.display.flip()