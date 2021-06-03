import pygame
from pygame import mixer
class Player():

    def __init__(self):
        self.Player_img = pygame.image.load('./Object_image/player.png')
        self.PlayerX = 370
        self.PlayerY = 480
        self.PlayerX_change = 0
        self.PlayerY_change = 0
        self.Player_speed = 5
        self.temp_playerspeed = 5
    def player_boundary(self):#thiet lap ranh gioi cho player
        if self.PlayerX >= 736:
            self.PlayerX = 736
        elif self.PlayerX <= 0:
            self.PlayerX = 0
        if self.PlayerY >= 536:
            self.PlayerY = 536
        elif self.PlayerY <= 0:
            self.PlayerY = 0
        #return self.PlayerX, self.PlayerY
    def draw_player(self,screen,x, y):
        screen.blit(self.Player_img, (x, y))
    def player_movement(self):
        self.PlayerX +=self.PlayerX_change
        self.PlayerY += self.PlayerY_change
    def player_direction(self,event_key):
        if event_key == pygame.K_LEFT:
            self.PlayerX_change = - self.Player_speed
        if event_key == pygame.K_RIGHT:
            self.PlayerX_change = self.Player_speed
        if event_key == pygame.K_UP:
            self.PlayerY_change = - self.Player_speed
        if event_key == pygame.K_DOWN:
            self.PlayerY_change = self.Player_speed
    def get_hit(self):
        explosion_sound = mixer.Sound('./Sound/explosion.wav')
        explosion_sound.play()
        explosion_sound.set_volume(0.2)



