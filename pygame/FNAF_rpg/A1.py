import pygame

a1pos = [[-1000, -1000], [300, -100], [200, 50], [300, 200], [-1000, -1000]]


cam1 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\cam.1.2.jpg')
a1 = pygame.image.load(r'C:\Users\kacpe\OneDrive\Obrazy\a.1.2.png')

       
def pov_cam1(screen, A):
    screen.blit(cam1, (0, 0))
    screen.blit(a1, a1pos[A[0]])
    pygame.display.flip()