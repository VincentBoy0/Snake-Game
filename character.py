import pygame
import setting
import color
import numpy as np
import random as rd
dx = [0, 0, -20, 20, 0]
dy = [-20, 20, 0, 0, 0]

class Fruit():
    def __init__(self, numberOfFruits = 30):
        List = []
        removeList = [[290, 230], [310, 230], [330, 230]]
        for i in range(60 + int(setting.cell_size / 2),540 - int(setting.cell_size/2),20):
            List.append(i)
        self.fruit = np.array([[800, 800]])
        flag = True
        i = 0
        while i < numberOfFruits:
            x = rd.choice(List)
            y = rd.choice(List)
            if [x,y] in removeList:
                flag = False
            else:
                flag = True
                self.fruit = np.append(self.fruit, [[x,y]], axis=0)     
                removeList.append([x,y])
            i += flag
            
        while flag == False:
                x = rd.choice(List)
                y = rd.choice(List)
                if [x,y] not in removeList:
                    flag = True
                    self.fruit = np.append(self.fruit, [[x,y]], axis=0)
        #print(len(self.fruit))
        
    def showFruit(self,screen):
        for i in range(len(self.fruit)):
            #print(self.fruit[i][0], self.fruit[i][1])
            pygame.draw.circle(screen, setting.colorFruit, (self.fruit[i][0], self.fruit[i][1]), setting.cell_size / 2)

    def collision(self, head):
        for i in range(len(self.fruit)):
            if head[0] == self.fruit[i][0] and head[1] == self.fruit[i][1]:
                self.fruit = np.delete(self.fruit, i, axis=0)
                return True
        return False

class Snake():
    def __init__(self, colorHead = color.RED, colorBody = color.WHITE):
        self.length = 3
        self.moved = 0
        self.colorHead = colorHead
        self.colorBody = colorBody
        self.list = np.array([[290, 230], [310, 230], [330, 230]])
        self.dir = 1
    def changeDir(self, dir):
        if self.dir == 0:
            if dir != 1:
                self.dir = dir
                self.moved = 0
        if self.dir == 1:
            if dir != 0:
                self.dir = dir
                self.moved = 0
        if self.dir == 2:
            if dir != 3:
                self.dir = dir
                self.moved = 0
        if self.dir == 3:
            if dir != 2:
                self.dir = dir
                self.moved = 0
    def draw(self, screen):
        for i, pos in enumerate(self.list):
            if i == 0:
                pygame.draw.circle(screen, self.colorHead, pos, 10)
            else:
                pygame.draw.circle(screen, self.colorBody, pos, 10)
    def move(self):
        # if self.moved == 1:
        #     return
        # self.moved = 1

        for i in range(len(self.list) - 1, 0, -1):
            if (i > 0):
                self.list[i] = self.list[i-1]
        self.list[0][0] += dx[self.dir]
        self.list[0][1] += dy[self.dir]
        
    def gameOver(self):
        if self.list[0][0] <= 60 or self.list[0][1] <= 60 or self.list[0][0] >= 560 or self.list[0][1] >= 560:
            return True
        for i in range(len(self.list)):
            if i > 0 and self.list[0][0] == self.list[i][0] and self.list[0][1] == self.list[i][1]:
                return True
        return False