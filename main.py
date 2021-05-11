import pygame

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init() #start pygame

#create a display screen: 400x400 pixels
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Rob's game")
done = False #we're not done displaying

while not done:
  for event in pygame.event.get(): #check the events list
    if event.type == pygame.QUIT: #if the user clicks the X0
      done = True #now we're done displaying
  #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

  screen.fill(WHITE)
  pygame.draw.rect(screen,RED,[0,0,50,80],0)
  #pygame.draw.line(screen,RED,[0,0],[50,80],width = 10)
  # https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
  pygame.draw.polygon(screen, RED, [(159,250),(50,55),(40,45)],0)
  pygame.display.update()

pygame.quit()

#import pygame