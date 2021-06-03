# pause/resume
# continue from last save
# play again when lost/win
# player Rank
import pygame
pygame.init()
class Board():
    def __init__(self):
        self.score_font = pygame.font.SysFont('bahnschrift',20)
        self.win_font = pygame.font.SysFont('bahnschrift', 64)
        self.GameOver_font = pygame.font.SysFont('bahnschrift', 64)
        self.Heart =pygame.image.load('./Object_image/like.png')
    def Scoreboard(self,x,y,score,scre):
        board = self.score_font.render("Score:" + str(score), True, (255, 255, 255))
        scre.blit(board, (x, y))
    def Winboard(self,x,y,scre):
        board = self.win_font.render("You win", True, (255, 255, 255))
        scre.blit(board, (x, y))
    def GameOverboard(self,x,y,scre):
        board = self.GameOver_font.render("Game Over", True, (255, 255, 255))
        scre.blit(board, (x, y))
    def Text(self,str,x,y,scre,size,color):
        self.Text_font = pygame.font.SysFont('bahnschrift',size)
        board = self.Text_font.render(str, True, color)
        scre.blit(board, (x, y))
    def draw_heart(self,lives,scre):
        dis = 0
        for i in range(lives):
            scre.blit(self.Heart,(736-dis,10))
            dis += 40
