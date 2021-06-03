import pygame
class Enemy():
    def __init__(self,speed,num):
        self.enemy_state = []
        self.Num = num
        self.enemy_img = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.tempX = []
        self.tempY = []
        self.spawnX = 0
        self.spawnY = 0
        for i in range(self.Num):
            self.enemy_state.append('alive')
            self.enemy_speed = speed
            self.enemy_img.append(pygame.image.load(self.img_path))
            self.enemyX.append(self.spawnX)
            self.enemyY.append(self.spawnY)
            self.enemyX_change.append(self.enemy_speed)
            self.enemyY_change.append(0)
            self.tempX.append(self.enemy_speed)
            self.tempY.append(self.enemy_speed/2)
            self.spawnX += + 70
            if i == (self.Num/2-1):
                self.spawnX = 0
                self.spawnY += 70
    def spawn(self):
        pass
    def enemy_movement(self,i):
        pass
    def draw_enemy(self,screen,x, y, i):
        screen.blit(self.enemy_img[i], (x, y))