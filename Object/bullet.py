import pygame
import math
class Bullet:

    def __init__(self):
        self.bullet_img = pygame.image.load('./Object_image/bullet.png')
        self.bulletX = 1000
        self.bulletY = 1000
        self.bulletY_change = 20
        self.temp_bulletspeed  = 20
        self.bullet_state = "ready"
    #bullet movement
    def bullet_fire(self,screen,x, y):
        global bullet_state
        self.bullet_state = "fire"
        screen.blit(self.bullet_img, (x + 16, y + 10))
    def Bulletstate(self,scre):
        if self.bulletY <= -10:
            self.bullet_state = "ready"
        if self.bullet_state == "fire":
            self.bullet_fire(scre, self.bulletX, self.bulletY)
            self.bulletY -= self.bulletY_change
