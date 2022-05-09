from abc import ABC, abstractmethod
import pygame,random
import time
from pygame.locals import *


# Environment Setting
windowW = 360
windowH = 640
FPS = 30

Obstacle_Width=80
Obstacle_Height=500
Obstacle_Gap=300
GROUND_HEIGHT =100
GROUND_WIDHT =2 * windowW

#font

# Game Setting
gravity = 0.5
characterSpeed = 7.5
GAME_SPEED=15
score=0

# Image Resource
backgroundGame = pygame.image.load("Assets/img/background-senja.png")
backgroundGame = pygame.transform.scale(backgroundGame,(windowW, windowH))
hpSprites = ["Assets/img/hp1.png",
             "Assets/img/hp2.png",
             "Assets/img/hp3.png"]

pygame.init()

font = pygame.font.SysFont('Bauhaus 93',45)
white=(255,234,0 )
screen = pygame.display.set_mode((windowW, windowH))
pygame.display.set_caption("FlappyMon - Character and Collision Implement")
clock = pygame.time.Clock()

class character(pygame.sprite.Sprite, ABC) :
    def __init__(self) :
        super().__init__()
        self.images = [pygame.image.load("Assets/img/swablue_up.png").convert_alpha(), 
                       pygame.image.load("Assets/img/swablue_normal.png").convert_alpha(), 
                       pygame.image.load("Assets/img/swablue_down.png").convert_alpha()]
                       
        self.current_img = 0
        self.image = self.images[self.current_img]
        self.rect = self.image.get_rect()
        self.rect.x = 35
        self.rect.y = int(windowH / 2)
        self.speed = characterSpeed

    def fallMove(self) :
        self.speed += gravity
        self.rect.y += self.speed
        self.current_img = (self.current_img + 1) % 3
        self.image = self.images[self.current_img]

    def moveUp(self) :
        self.speed = -characterSpeed

    
    def get_score(self,point):
        Pos_Detection=False
        if pokeObject.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left\
            and pokeObject.sprites()[0].rect.right<pipe_group.sprites()[0].rect.right\
                and Pos_Detection==False:
                    Pos_Detection=True
        if Pos_Detection== True: 
            if pokeObject.sprites()[0].rect.left < pipe_group.sprites()[0].rect.right:

                point+=1
                print(point)
                
        return point
         

    @abstractmethod
    def castSkill() :
        pass

    @abstractmethod
    def drownHP() :
        pass

    @abstractmethod
    def getHP() :
        pass

class poke1(character) :
    def __init__(self) :
        super().__init__()
        self.__hp = 3
   
    def castSkill(self) :
        pass

    def drownHP(self):
        self.__hp -= 1
    
    def getHP(self) :
        return self.__hp

class poke2(character) :
    def __init__(self) :
        super().__init__()
        self.__hp = 3
    
    def castSkill(self) :
        pass

    def drownHP(self):
        self.__hp -= 1
    
    def getHP(self) :
        return self.__hp


class poke3(character) :
    def __init__(self) :
        super().__init__()
        self.__hp = 3
    
    def castSkill(self) :
        pass

    def drownHP(self):
        self.__hp -= 1

    def getHP(self) :
        return self.__hp


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize,img_dir):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Obstacle_Width, Obstacle_Height))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = Obstacle_Height - ysize
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect[0] -= GAME_SPEED

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, xpos,image_dir):
        super().__init__()
        self.image = pygame.image.load(image_dir).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDHT, GROUND_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = windowH - GROUND_HEIGHT
    def update(self):
        self.rect[0] -= GAME_SPEED

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    Obs = Obstacle(False, xpos, size,'Assets/img/twilight-obstacle.png')
    Obs_inverted = Obstacle(True, xpos, windowH - size - Obstacle_Gap,'Assets/img/twilight-obstacle.png')
    return Obs, Obs_inverted

def show_score(text,font,color,x,y):
    img=font.render(text,True,color)
    screen.blit(img  ,(x,y))

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


pokeObject = pygame.sprite.Group()
pikachu = poke2()        
pokeObject.add(pikachu)

ground_group = pygame.sprite.Group()

for i in range (2):
    ground = Ground(GROUND_WIDHT * i,'Assets/img/bases.png')
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()
for i in range (2):
    pipes = get_random_pipes(windowW * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])


isGameRun = True
after_collide = False
after_collide_interval = 5

while isGameRun :
    clock.tick(FPS)

    for event in pygame.event.get() :
        if(event.type == QUIT) :
            isGameRun = False
        if(event.type == KEYDOWN) :
            if(event.key == K_SPACE or event.key == K_UP):
                pikachu.moveUp()

    if(pikachu.getHP() == 3) :
        hpImg = pygame.image.load(hpSprites[2])
        hpImg = pygame.transform.scale(hpImg, (47,20))
    elif(pikachu.getHP() == 2) :
        hpImg = pygame.image.load(hpSprites[1])
        hpImg = pygame.transform.scale(hpImg, (33,20))
    else :
        hpImg = pygame.image.load(hpSprites[0])
        hpImg = pygame.transform.scale(hpImg, (20,20))
    
    pikachu.fallMove()
    screen.blit(backgroundGame, (0,0))
    screen.blit(hpImg, (0,5))
    pokeObject.update()
    pokeObject.draw(screen)
    screen.blit(backgroundGame, (0, 0))
    screen.blit(hpImg, (0,5))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(GROUND_WIDHT - 20,'Assets/img/bases.png')
        ground_group.add(new_ground)
    
    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = get_random_pipes(windowW * 2)

        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    ground_group.update()
    pipe_group.update()

    pokeObject.draw(screen)
    pipe_group.draw(screen)
    ground_group.draw(screen)
    

    if len(pipe_group)>0:
        score=pikachu.get_score(score)
    show_score(str(score),font ,white,int(windowW/2)-30,20)
    
    pygame.display.update()
    pygame.display.flip()
    if(pygame.sprite.groupcollide(pokeObject, ground_group, False,False, pygame.sprite.collide_mask)) :
        if(pikachu.getHP() == 0) :  
            time.sleep(1)
            break
        pikachu.drownHP()
        pikachu.rect.x = 35
        pikachu.rect.y = int(windowH / 2) - 20
        pikachu.speed = characterSpeed
        continue

    if (pygame.sprite.groupcollide(pokeObject, pipe_group, False, False, pygame.sprite.collide_mask)):
        
        if(pikachu.getHP() == 0) :  
            time.sleep(1)
            break
        
        if(after_collide) :
            after_collide_interval -= 1
            if(after_collide_interval == 0) :
                after_collide = False
                after_collide_interval = 5 
            continue
        else :
            pikachu.drownHP()
            after_collide = True
            continue


pygame.quit()