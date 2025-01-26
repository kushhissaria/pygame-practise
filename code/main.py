import pygame
from os.path import join
from random import randint
pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT=1280,720
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT) )
pygame.display.set_caption("Space Shooter")
running= True
#plain surface
surf=pygame.Surface((200,150))
surf.fill("yellow")
x=100

#importing an image
player_surf=pygame.image.load(join("images","player.png")).convert_alpha()
star_surf=pygame.image.load(join("images","star.png")).convert_alpha()
star_pos=[(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20) ]
'''print(star_pos)
for i,j in star_pos:
  print(i)'''

while running:
  # event loop  
    for event in pygame.event.get(): 
      print(event)
      if event.type==pygame.QUIT:
        running= False
  
  # draw surface
    display_surface.fill("darkgray")
    x+=0.1
    
    display_surface.blit(player_surf,(x,150))
    
    for i,j in star_pos:
     display_surface.blit(star_surf,(i,j))
     
    pygame.display.update()
pygame.quit()  