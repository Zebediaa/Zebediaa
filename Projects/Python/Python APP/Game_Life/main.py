import pygame
import os
from pygame_game_life import *
import numpy as np


os.environ["SDL_VIDEO_CENTERED"] = '1'


width, height = 1600, 1400
# width, height = 1920, 1080
size = (width,height)

pygame.init()
pygame.display.set_caption("Game Of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 240

black = (0,0,0)
white = (255,255,255)

scale = 40
offset = 1


Grid = Game_Life(width,height,scale,offset,color_alive=white,color_dead=black,surface=screen)
Grid.white()


run = True
go = True


while run:
    clock.tick(fps)
    screen.fill(black)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and go == False:
                go = True
            else:
                go  = False
            if event.key == pygame.K_c:
                Grid.white()
                go = True
            if event.key == pygame.K_d:
                x = pygame.mouse.get_pos()
                Grid.glider(x[0],x[1])
                go = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("YEAH")
            x = pygame.mouse.get_pos()
            # print(x[0])
            # print(x[1])
            Grid.colored(x[0],x[1])

    Grid.test(go)


    pygame.display.update()

pygame.quit()

#
