import pygame
from Object import *
class Enemy1(Enemy):
    def __init__(self,num,speed):
        self.img_path = './Object_image/enemy.png'
        Enemy.__init__(self, num, speed)

    def enemy_movement(self,i):
        if self.enemyX[i] < 0 or self.enemyX[i] >= 736:
            self.enemyX_change[i] = - self.enemyX_change[i]
            self.tempX[i] = self.enemyX_change[i]
            self.enemyY_change[i] += 64
        self.enemyX[i] += self.enemyX_change[i]
        self.enemyY[i] += self.enemyY_change[i]
        self.enemyY_change[i] = 0
        return self.enemyX[i], self.enemyY[i]
