import pygame
import random

#Initialize pygame
pygame.init()

# Add events
Sprite_Color_Changing_Event= pygame.USEREVENT+1
Backround_Color_Changing_Event= pygame.USEREVENT+2

# backround colors
blue=pygame.color('blue')
light_blue=pygame.color('light blue')
dark_blue=pygame.color('dark blue')

# Sprite colors
yellow=pygame.color('yellow')
magenta=pygame.color('magenta')
orange=pygame.color('orange')
white=pygame.color('white')

# class  for movement of th sprite
class Sprite:
    
    def __init__(self,color,height,width):
        super().__init__()
        self.image =pygame.Surface([height,width])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
        
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]= -self.velocity[0]
            boundry_hit=True
            
        if self.rect.top<=0 or self.rect.bottom>=400:
             self.velocity[1]= -self.velocity[1]
             boundry_hit=True
             
        if boundry_hit:
            pygame.event.post(pygame.event.Event(Sprite_Color_Changing_Event))
            pygame.event.post(pygame.event.Event(Backround_Color_Changing_Event))
            
    def change_color(self):
        self.image.fill(random.choice([yellow,magenta,orange,white]))

def change_backround(self):
    global bg_color
    bg_color=random.choice([blue,light_blue,dark_blue])
    
sprite_list=pygame.sprite.Group()
sp1=Sprite(white,20,30)
sp1.rect.x=random.randint(0,480)   
sp1.rect.y=random.randint(0,370)
sprite_list.add(sp1)

screen=pygame.pygame.display.set_mode((400,500,))
pygame.display.set_caption('Boundry Sprite')
bg_color=blue
screen.fill(bg_color)
exit=False
clock=pygame.time.clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
            
        elif event.type==Sprite_Color_Changing_Event:
            sp1.change_color()
            
        elif event.type==Backround_Color_Changing_Event:
            change_backround() 
            
    sprite_list.update()
    screen.fill(bg_color)
    sprite_list.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(240)
    
pygame.quit()
                    