import time
import pygame, random as rd
from Object import *
import pickle
from Game_Config import *
from pygame import mixer
import math
board =Board()
class GameState():
    def __init__(self):
        self.game_over = False
        self.game_state = 'playing'
        self.game_start = False
        self.game_replay = False
        self.game_win = False
        self.get_hit = False
        self.win_save = False
        self.watching =False
    #Pause Game
    def Game_Pause(self,pl,bul,ene1,ene2):
        self.game_state = 'pausing'
        bul.bulletY_change = 0
        pl.Player_speed = 0
        for i in range(ene1.Num):
            ene1.enemyX_change[i] = 0
        for i in range(ene2.Num):
            ene2.enemyX_change[i] = 0
            ene2.enemyY_change[i] = 0

    # ham xu ly va cham
    def iscollision(self,Obj1_X, Obj1_Y, Obj2_X, Obj2_Y, dis):
        distance = math.sqrt(math.pow(Obj1_X - Obj2_X, 2) + math.pow(Obj1_Y - Obj2_Y, 2))
        if distance <= dis:
            return True
        else:
            return False
    def got_hit(self):
        explosion_sound = mixer.Sound('./Sound/explosion.wav')
        explosion_sound.play()
        explosion_sound.set_volume(0.2)
    def Game_Resume(self,pl,bul,ene1,ene2):
        self.game_state = 'playing'
        pl.Player_speed = pl.temp_playerspeed
        bul.bulletY_change = bul.temp_bulletspeed
        for i in range(ene1.Num):
            ene1.enemyX_change[i] = ene1.tempX[i]
        for i in range(ene2.Num):
            ene2.enemyX_change[i] = ene2.tempX[i]
            ene2.enemyY_change[i] = ene2.tempY[i]
        print(ene2.enemyY_change[i])
    # màn hình khởi động đầu game
    def Game_StartScreen(self,scre,pl,bul,ene1,ene2):
        scre.fill((0,178,191))
        board.Text("Enter  ---  Play", 250, 300, scre, 30,(255, 255, 255))
        board.Text("Player: ",150,250,scre,30,(255, 255, 255))
        board.Text("F1  ------  Continue", 250,350, scre, 30,(255, 255, 255))

        bul.bulletY_change = 0
        pl.Player_speed = 0
        bul.bulletY_change = 0
        pl.Player_speed = 0
        for i in range(ene1.Num):
            ene1.enemyX_change[i] = 0
        for i in range(ene2.Num):
            ene2.enemyX_change[i] = 0
            ene2.enemyY_change[i] = 0
    # Âm thanh khi va chạm
    def got_hit(self):
        explosion_sound = mixer.Sound('./Sound/explosion.wav')
        explosion_sound.play()
        explosion_sound.set_volume(0.2)
    # hàm xử lý va chạm
    def iscollision(self,Obj1_X, Obj1_Y, Obj2_X, Obj2_Y, dis):
        distance = math.sqrt(math.pow(Obj1_X - Obj2_X, 2) + math.pow(Obj1_Y - Obj2_Y, 2))
        if distance <= dis:
            return True
        else:
            return False
    #Bắt đầu game
    def Game_Play(self,pl,bul,ene1,ene2):
        self.game_start = True
        self.game_state ="playing"
        pl.Player_speed = pl.temp_playerspeed
        bul.bulletY_change = bul.temp_bulletspeed
        for i in range(ene1.Num):
            ene1.enemyX_change[i] = ene1.tempX[i]
        for i in range(ene2.Num):
            ene2.enemyX_change[i] = ene2.tempX[i]
            ene2.enemyY_change[i] = ene2.tempY[i]

    def Game_save(self,pl,bul,enem1,enem2,lives,player_name,score):
        savefile = open("./GameFile/Save.txt",'w')
        savefile.write(player_name + "\n")
        savefile.write(str(pl.PlayerX)+"\n")
        savefile.write(str(pl.PlayerY)+"\n")
        savefile.write(str(bul.bullet_state)+"\n")
        savefile.write(str(lives)+"\n")
        savefile.write(str(score)+"\n")
        #enemy1
        for i in range(enem1.Num):
            savefile.write(str(enem1.enemyX[i])+"\n")
            savefile.write(str(enem1.enemyY[i]) + "\n")
            savefile.write(str(enem1.enemyX_change[i]) + "\n")
            savefile.write(str(enem1.enemyY_change[i]) + "\n")
        savefile.write(str(enem1.enemy_speed) + "\n")
        #enemy2
        for j in range(enem2.Num):
            savefile.write(str(enem2.enemyX[j]) + "\n")
            savefile.write(str(enem2.enemyY[j]) + "\n")
            savefile.write(str(enem2.enemyX_change[j]) + "\n")
            savefile.write(str(enem2.enemyY_change[j]) + "\n")
        savefile.write(str(enem2.enemy_speed) + "\n")
        savefile.close()
        '''
    def Game_save(self,object):
        savefile = open("./GameFile/Save.txt",'w')
        pickle.dump(object)
        savefile.close()'''
    def Game_continue(self,pl,bul,enem1,enem2):
        filegame =open("./GameFile/Save.txt",'r')
        player_name = filegame.readline()
        pl.PlayerX = int(filegame.readline())
        pl.PlayerY = int(filegame.readline())
        bul.bullet_state = filegame.readline()
        lives = int(filegame.readline())
        score = int(filegame.readline())

        for i in range(enem1.Num):
            enem1.enemyX[i] = int(filegame.readline())
            enem1.enemyY[i] = int(filegame.readline())
            enem1.enemyX_change[i] =int(filegame.readline())
            enem1.enemyY_change[i] =int(filegame.readline())
        enem1.enemy_speed =int(filegame.readline())
        for j in range(enem2.Num):
            enem2.enemyX[j] = int(filegame.readline())
            enem2.enemyY[j] =float(filegame.readline())
            enem2.enemyX_change[j] =int(filegame.readline())
            enem2.enemyY_change[j] =float(filegame.readline())
        enem2.enemy_speed =int(filegame.readline())
        filegame.close()
        return lives,player_name,score
    def Game_win(self,screen):
            self.game_win = True
            board.Winboard(300, 250, screen)
            board.Text("Press R to replay", 250, 350, screen,40,(255, 255, 255))
    def Player_rank(self,Player_name,win_times):
        self.win_save =True
        loop = 0
        filegame = open("./GameFile/Rank.txt", 'r+')
        player_list = filegame.read().splitlines()
        filegame.close()
        filegame = open("./GameFile/Rank.txt", 'w+')
        for i in range(0, len(player_list),2):
            if Player_name == player_list[i]:
                loop =1
                player_list[i+1] = int(player_list[i + 1]) + 1
                break
        if loop ==0:
            player_list.append(Player_name)
            player_list.append(win_times)
        for i in range(len(player_list)):
            filegame.write(str(player_list[i]) + "\n")
        filegame.close()
    def Show_rank(self,scre):
        scre.fill((0,178,191))
        player_wintimes=[]
        top_5=[]
        filegame = open("./GameFile/Rank.txt", 'r+')
        player_list = filegame.read().splitlines()
        filegame.close()
        board.Text("Player        Wins",140,100,scre,64,(16,54,103))
        for i in range(1,len(player_list),2):
            player_wintimes.append(-1)
            player_wintimes.append(int(player_list[i]))
        s = 60
        for j in range(5):
            for k in range(len(player_list)-1):
                if int(player_wintimes[k+1]) == max(player_wintimes):
                    board.Text(str(player_list[k]), 150, 100 + s, scre, 40, (16,54,103))
                    board.Text(str(player_list[k + 1]), 500, 100 + s, scre, 40,(16,54,103))
                    top_5.append(player_wintimes[k+1])
                    player_wintimes[k+1] = -1
                    s+= 50
                    break









