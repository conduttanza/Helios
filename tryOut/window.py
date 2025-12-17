#code by conduttanza
#
#created the 17/12/2025

#universal imports
import pygame, numpy as np

#self made imports
import logic, inputs, imagRec_logic

config = logic.Config()
code = logic.Logic()
fps = config.fps
side = config.side

side_x = side
side_y = side

pygame.init()
pygame.display.set_caption('project x')
screen = pygame.display.set_mode((side_x, side_y))
clock = pygame.time.Clock()

def func(code):
    code.outPut(1)
    
running = True

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('quitting...')
            
        screen.fill((0,0,0))
        func(code)
        clock.tick(fps)
        
        if running == False:
            print('pygame quit successfully')

except KeyboardInterrupt:
    pygame.quit()
    print('kb quit successful')
    running = False