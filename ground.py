import pygame
from pygame.locals import *

Lebar_Window = 400
Tinggi_Window = 600
GAME_SPEED = 10
FPS = 30
Lebar_lantai = 2 * Lebar_Window
Tinggi_lantai= 100

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/bases.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (Lebar_lantai, Tinggi_lantai)) 

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = Tinggi_Window - Tinggi_lantai
        
    def update(self):
        self.rect[0] -= GAME_SPEED

def Kontrol_layar(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()
Layar = pygame.display.set_mode((Lebar_Window, Tinggi_Window))
pygame.display.set_caption('Flappy Mon')

BACKGROUND = pygame.image.load('assets/sprites/background-senja.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (Lebar_Window, Tinggi_Window))

ground_group = pygame.sprite.Group()

for i in range (2):
    ground = Ground(Lebar_lantai * i)
    ground_group.add(ground)

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    Layar.blit(BACKGROUND, (0, 0))
    if Kontrol_layar(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(Lebar_lantai - 20)
        ground_group.add(new_ground)

    ground_group.update()
    ground_group.draw(Layar)

    pygame.display.update()

