import time
import pygame, random as rd
from Object import *
from Game_Config import *
from pygame import mixer
import math

rd.seed(0)
pygame.init()

# tao man hinh kich thuoc 800*600
screen = pygame.display.set_mode((800, 600))

# icon va caption
pygame.display.set_caption("Shooting Game!")
icon = pygame.image.load('./Object_image/Space-invader.png')
pygame.display.set_icon(icon)
explosion = pygame.image.load('./Object_image/explosion.png')
background = pygame.image.load('./Object_image/background.jpg')
pause_button = pygame.image.load('./Object_image/pause-button.png')

# diem so
score = 0
fps = 60
# khoi tao cac doi tuong
player = Player()
enem_1 = Enemy1(5,10)
enem_2 = Enemy2(5,5)


bullet = Bullet()
board = Board()
input_box1 = InputBox(250,250,140, 32)
input_boxes = [input_box1]
gamestate = GameState()
clock =pygame.time.Clock()

# Background music
mixer.music.load('./Sound/background.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.3)

# ham xu ly va cham
def iscollision(Obj1_X, Obj1_Y, Obj2_X, Obj2_Y, dis):
    distance = math.sqrt(math.pow(Obj1_X - Obj2_X, 2) + math.pow(Obj1_Y - Obj2_Y, 2))
    if distance <= dis:
        return True
    else:
        return False
count = 1
win_times = 1
start =pygame.time.get_ticks()
Lives = 3

# loop update
running = True
while running:
    clock.tick(fps)

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for box in input_boxes:
            box.handle_event(event,gamestate.game_start)

        if event.type == pygame.KEYDOWN:
            # Return game
            if event.key == pygame.K_r:
                if (gamestate.game_over == True or gamestate.game_win == True or gamestate.game_state == 'pausing'):
                    gamestate.game_replay = True
            # Start game
            if event.key == pygame.K_RETURN:
                gamestate.Game_Play(player, bullet, enem_1, enem_2)
            # show Player Rank
            if event.key == pygame.K_w and (gamestate.game_win ==True or gamestate.game_start ==False or gamestate.game_state =="pausing"):
                gamestate.watching =True
            if event.key == pygame.K_c and gamestate.watching ==True:
                gamestate.watching =False

            # Play from last save
            if event.key == pygame.K_F1 and gamestate.game_start == False:
                gamestate.Game_Play(player, bullet, enem_1, enem_2)
                Lives,player_name,score = gamestate.Game_continue(player, bullet, enem_1, enem_2)
                bullet.bullet_state ='ready'
            # Pause & Save game
            if event.key == pygame.K_ESCAPE and gamestate.game_state == "playing":
                gamestate.Game_save(player, bullet, enem_1, enem_2, Lives, player_name, score)
                gamestate.Game_Pause(player, bullet, enem_1, enem_2)
            # Resume game
            if event.key == pygame.K_RETURN and gamestate.game_state == "pausing":
                gamestate.Game_Resume(player, bullet, enem_1, enem_2)

            player.player_direction(event.key)
            # Bắn đạn
            if event.key == pygame.K_SPACE:
                if bullet.bullet_state == "ready":
                    bullet_sound = mixer.Sound('./Sound/laser.wav')
                    bullet_sound.play()
                    bullet_sound.set_volume(0.5)
                    bullet.bulletX = player.PlayerX
                    bullet.bulletY = player.PlayerY
                    bullet.bullet_fire(screen, bullet.bulletX, bullet.bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.PlayerX_change = 0
                player.PlayerY_change = 0
    player_name = str(input_boxes[0].text)
    box.update()


    if score < enem_1.Num * 10:
        for i in range(enem_1.Num * count):
            collision1 = iscollision(enem_1.enemyX[i], enem_1.enemyY[i], bullet.bulletX, bullet.bulletY, 30)
            colli_player1 = iscollision(enem_1.enemyX[i], enem_1.enemyY[i], player.PlayerX, player.PlayerY, 50)
            if colli_player1:
                gamestate.get_hit = True
                gamestate.got_hit()
            enem_1.enemyX[i], enem_1.enemyY[i] = enem_1.enemy_movement(i)
            # xu ly va cham enemy ,bullet
            if collision1:
                # Am thanh khi bullet va cham voi enemy
                gamestate.got_hit()
                enem_1 .enemy_state[i] = 'slayed'
                bullet.bulletX = 1000
                bullet.bulletY = 1000
                bullet.bullet_state = "ready"
                score += 10
                enem_1.enemyX[i] = 600
                enem_1.enemyY[i] = 800
                enem_1.enemyX_change[i] = 0

            enem_1.draw_enemy(screen, enem_1.enemyX[i], enem_1.enemyY[i], i)
    else:
        for j in range(enem_2.Num):
            collision2 = gamestate.iscollision(enem_2.enemyX[j], enem_2.enemyY[j], bullet.bulletX, bullet.bulletY, 30)
            colli_player2 = gamestate.iscollision(enem_2.enemyX[j], enem_2.enemyY[j], player.PlayerX, player.PlayerY, 50)
            if colli_player2:
                gamestate.get_hit = True
                gamestate.got_hit()

            # enemy2 movement
            enem_2.enemyX[j], enem_2.enemyY[j] = enem_2.enemy_movement(j)

            # xu ly va cham enemy, bullet
            if collision2:
                # Am thanh khi bullet va cham voi enemy
                gamestate.got_hit()
                enem_2.enemy_state[j] = 'slayed'
                bullet.bulletX = 1000
                bullet.bulletY = 1000
                bullet.bullet_state = "ready"
                score += 10
                enem_2.enemyX[j] = 600
                enem_2.enemyY[j] = 800
            enem_2.draw_enemy(screen, enem_2.enemyX[j], enem_2.enemyY[j], j)
    if gamestate.get_hit == True:
        gamestate.get_hit =False
        Lives -= 1
        player.PlayerX = 370
        player.PlayerY = 480


    # game over check
    if Lives ==0:
        gamestate.game_over = True
    if gamestate.game_over == True:
        # In bang "Game over"
        screen.blit(explosion,(player.PlayerX,player.PlayerY))
        player.PlayerX_change = 0
        player.PlayerY_change = 0
        bullet.bullet_state = 'fire'
        board.GameOverboard(200, 250, screen)
        board.Text("Press R to replay", 200, 350, screen, 40,(255, 255, 255))
        for i in range(enem_1.Num):
            enem_1.enemyX[i] = 801
            enem_1.enemyY[i] = 601
        for i in range(enem_2.Num):
            enem_2.enemyX[i] = 801
            enem_2.enemyY[i] = 601
    #game replay run
    if (gamestate.game_over == True or gamestate.game_win ==True or gamestate.game_state =='pausing') and gamestate.game_replay ==True:
        gamestate.game_replay = False
        gamestate.game_over =False
        gamestate.game_win = False
        gamestate.Game_Resume(player, bullet, enem_1, enem_2)
        bullet.bullet_state ='ready'
        enem_1 = Enemy1(5,10)
        enem_2 = Enemy2(5,5)
        player.PlayerX =370
        player.PlayerY =480
        score = 0
        Lives = 3
    if gamestate.game_over == False:
        player.draw_player(screen, player.PlayerX, player.PlayerY)

    if gamestate.game_start == False:
        gamestate.Game_StartScreen(screen, player, bullet, enem_1, enem_2)
        for box in input_boxes:
            box.draw(screen)

    # player boundary
    player.player_boundary()
    # player movement
    player.player_movement()
    # show lives
    board.draw_heart(Lives,screen)
    # xu ly trang thai cua bullet(state)
    bullet.Bulletstate(screen)
    # in bang diem so
    board.Scoreboard(10, 10, score, screen)
    # Game win
    if score == enem_1.Num * 10 + enem_2.Num * 10:
        gamestate.Game_win(screen)
        #neu game chua save thi se tu dong save
        if gamestate.win_save == False:
            gamestate.Player_rank(player_name,win_times)
    # Game Pause
    if gamestate.game_state == "pausing":
        screen.fill((0,178,191))
        screen.blit(pause_button, (350, 200))
        board.Text("Press Enter to resume", 190, 310, screen, 40,(16,54,103))
        board.Text("Press R to replay", 240, 410, screen, 40,(16,54,103))
    if gamestate.watching ==True :
        gamestate.Show_rank(screen)

    pygame.display.update()
pygame.quit()
