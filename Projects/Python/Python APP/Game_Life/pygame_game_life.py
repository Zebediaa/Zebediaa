import numpy as np
import matplotlib.pyplot as plt
import pygame
import time

class Game_Life:

    def __init__(self,width,height,scale,offset,color_alive,color_dead,surface):
        self.scale = scale*0.5
        self.rows = int(width*2/scale)
        self.columns = int(height*2/scale)
        grid = np.ndarray(shape = (self.rows,self.columns))
        self.grid = np.pad(grid, 1, mode = 'constant')
        self.offset = offset
        self.alive = color_alive
        self.dead = color_dead
        self.surface = surface

# """
# See if this generation of this cell is evolving
# """

    def generation(self,value,neig):
        # print('hit')
        if value == 1:
            # print('hit')
            if neig < 2:
                return False
            elif neig == 2 or neig == 3:
                # print("touch")
                return True
            elif neig > 3:
                return False

        else:

            if neig == 3:
                return True

# """
# Count the number of neighbour
# """

    def neighbour(self,value,row,column):
        m=0
        for i in range(3):
            for k in range(3):
                if 1 == self.grid[(row-1) + i][(column-1) + k]:
                    m += 1
        if self.grid[row][column] == 1:
            m-=1
        # print(m)
        return m

    def white(self):
        for i in range(self.rows):
            for k in range(self.columns):
                self.grid[i][k] = 0

        # self.grid[8][10] = 1
        # self.grid[8][9] = 1
        # self.grid[8][8] = 1


    def colored(self,x,y):
        i = int(x/self.scale)
        k = int(y/self.scale)
        # print(f"self.grid[{i}][{k}] = 1")
        # print(k)
        if self.grid[i][k] == 0:
            self.grid[i][k] = 1
        else:
            self.grid[i][k] = 0


    def glider(self,x,y):
        i = int(x/self.scale)
        k = int(y/self.scale)

        try:

            self.grid[11+i-11][21+k-21] = 1
            self.grid[11+i-11][22+k-21] = 1
            self.grid[12+i-11][22+k-21] = 1
            self.grid[12+i-11][21+k-21] = 1
            self.grid[21+i-11][22+k-21] = 1
            self.grid[21+i-11][21+k-21] = 1
            self.grid[21+i-11][23+k-21] = 1
            self.grid[22+i-11][24+k-21] = 1
            self.grid[23+i-11][25+k-21] = 1
            self.grid[24+i-11][25+k-21] = 1
            self.grid[22+i-11][20+k-21] = 1
            self.grid[23+i-11][19+k-21] = 1
            self.grid[24+i-11][19+k-21] = 1
            self.grid[25+i-11][22+k-21] = 1
            self.grid[26+i-11][20+k-21] = 1
            self.grid[27+i-11][21+k-21] = 1
            self.grid[27+i-11][22+k-21] = 1
            self.grid[27+i-11][23+k-21] = 1
            self.grid[28+i-11][22+k-21] = 1
            self.grid[26+i-11][24+k-21] = 1
            self.grid[31+i-11][21+k-21] = 1
            self.grid[31+i-11][20+k-21] = 1
            self.grid[31+i-11][19+k-21] = 1
            self.grid[32+i-11][19+k-21] = 1
            self.grid[32+i-11][20+k-21] = 1
            self.grid[32+i-11][21+k-21] = 1
            self.grid[33+i-11][18+k-21] = 1
            self.grid[33+i-11][22+k-21] = 1
            self.grid[35+i-11][18+k-21] = 1
            self.grid[35+i-11][17+k-21] = 1
            self.grid[35+i-11][22+k-21] = 1
            self.grid[35+i-11][23+k-21] = 1
            self.grid[45+i-11][20+k-21] = 1
            self.grid[46+i-11][20+k-21] = 1
            self.grid[46+i-11][21+k-21] = 1
            self.grid[45+i-11][21+k-21] = 1
        except IndexError:
            print("nop")
# """
# See if this generation of this cell is evolving
# """

    def test(self,go):


        if go:

            for i in range(self.rows):
                for k in range(self.columns):
                    if self.grid[i][k] == 1:
                        pygame.draw.rect(self.surface,self.dead,[i*self.scale,k*self.scale,self.scale-self.offset,self.scale-self.offset])
                    else:
                        pygame.draw.rect(self.surface,self.alive,[i*self.scale,k*self.scale,self.scale-self.offset,self.scale-self.offset])

        else :

            neig = np.zeros((self.rows, self.columns))

            for i in range(self.rows):
                for k in range(self.columns):
                    v = self.grid[i][k]
                    neig[i][k] = int(self.neighbour(v,i,k))
                    # print(f"{i},{k},{v},{neig[i][k]}")

            for i in range(self.rows):
                for k in range(self.columns):
                    if self.generation(self.grid[i][k],int(neig[i][k])):
                        self.grid[i][k] = 1
                        # print("ok")
                        pygame.draw.rect(self.surface,self.dead,[i*self.scale,k*self.scale,self.scale-self.offset,self.scale-self.offset])
                    else:
                        self.grid[i][k] = 0
                        pygame.draw.rect(self.surface,self.alive,[i*self.scale,k*self.scale,self.scale-self.offset,self.scale-self.offset])









        #
