import pygame
from Object import *
class Enemy2(Enemy):
    def __init__(self,num,speed):
        self.img_path = './Object_image/enemy2.png'
        Enemy.__init__(self, num, speed)
    def enemy_movement(self,j):
        self.enemyY_change[j] = self.tempY[j]
        if self.enemyX[j] < 0 or self.enemyX[j] >= 736:
            self.enemyX_change[j] = - self.enemyX_change[j]
            self.tempX[j] = self.enemyX_change[j]

        if (self.enemyY[j] <= 0 or self.enemyY[j] >= 536) and self.enemy_state[j] =='alive' :
            self.enemyY[j] = 0
        self.enemyX[j] += self.enemyX_change[j]

        self.enemyY[j] += self.enemyY_change[j]
        return self.enemyX[j],self.enemyY[j]
