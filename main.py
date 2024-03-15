import pygame
from color import PURPLE, ORANGE, BLACK, BLUE, YELLOW, GREEN, GREY, PINK, MINT, WHITE, RED
from setting import screen_height, screen_width
from setting import background_intro, exit
from setting import iconImg, mouseClickSound
from character import Snake
from continueGame import foodArray, checkContinue, colorBody, colorHead, levelGame
pygame.init()
import numpy as np
#Caption and Icon
pygame.display.set_icon(iconImg)
pygame.display.set_caption("Snake Game")

#Text
titleFont = pygame.font.Font('freesansbold.ttf', 60)
titleText = titleFont.render('Snake Game', True, WHITE)
titleRect = titleText.get_rect(center = (300,200))

font = pygame.font.Font('freesansbold.ttf', 32)
play = font.render('Next', True, WHITE)
playRect = play.get_rect(center = (195, 405))

ctn = font.render('Continue', True, WHITE)
ctnRect = ctn.get_rect(center = (420, 405))

cancel = font.render('Cancel', True, WHITE)
cancelRect = cancel.get_rect(center = (305, 485))

easy = font.render('Easy', True, WHITE)
easyRect = easy.get_rect(center = (310, 150))

normal = font.render('Normal', True, WHITE)
normalRect = normal.get_rect(center = (310, 150))

hard = font.render('Hard',  True, WHITE)
hardRect = hard.get_rect(center = (310, 150))

#----------Character------------------
snake_list = [Snake(RED, WHITE), Snake(PURPLE, BLUE), Snake(MINT, PINK)]
color_snake = [[RED, WHITE], [PURPLE, BLUE], [MINT, PINK]]
level = [[easy, easyRect, 6, 30], [normal, normalRect, 8, 50], [hard, hardRect, 10, 70]]
#-------------------------------
def inside(pos, rect):
    return rect[0] <= pos[0] and pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] and pos[1] <= rect[1] + rect[3]

#-------------------------------

running = 1
menu = True
setting_screen = False
while running:
    ctn_check = 0
    screen = pygame.display.set_mode((screen_width, screen_height))
    setting, playing = False, False
    cnt1, cnt2 = 0, 0
    sz1, sz2 = 3, 3
    ctn_check = 0
    checkExit = 0
    while running == True and menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                checkExit = 1
                #running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickSound.play()
                if event.button == 1:             
                    print(event.pos)
                    if checkExit == 1:
                        if inside(event.pos, (310, 45, 135, 35)):
                            running = False
                        if inside(event.pos, (455, 45, 135, 35)):
                            checkExit = 0           
                    if inside(event.pos, (120, 370, 160, 70)):
                        if setting_screen == False:
                            setting_screen = True
                            playing = False
                        else:
                            playing = True 
                            setting_screen = False    
                    elif setting_screen == True:
                        if rect2.collidepoint(event.pos):
                            cnt1 += 1
                        if rect1.collidepoint(event.pos):
                            cnt1 -= 1
                        if rect3.collidepoint(event.pos):
                            cnt2 -= 1
                        if rect4.collidepoint(event.pos):
                            cnt2 += 1             
                    if inside(event.pos, (230, 450, 160, 70)):
                        running = False
                    if inside(event.pos, (340, 370, 160, 70)) and setting_screen == False:
                        if checkContinue():
                            ctn_check = 1
                            playing = True
                        
        screen.blit(background_intro, (0, 0))
        pygame.draw.rect(screen, WHITE, (120, 370, 160, 70), 4) #Next
        pygame.draw.rect(screen, WHITE, (340, 370, 160, 70), 4) #Continue
        pygame.draw.rect(screen, WHITE, (230, 450, 160, 70), 4) #Cancel
        screen.blit(titleText,titleRect)
        screen.blit(play, playRect)
        screen.blit(cancel,cancelRect)
        screen.blit(ctn, ctnRect)
        #------------Setting screen------------------
        if setting_screen == True:
            if cnt1 < 0:
                cnt1 += sz1
            if cnt1 >= sz1:
                cnt1 %= sz1
            if cnt2 < 0:
                cnt2 += sz2
            if cnt2 >= sz2:
                cnt2 %= sz2
            pygame.draw.rect(screen, GREY, (30, 50, 540, 300))
            rect1 = pygame.draw.polygon(screen, YELLOW, ((200, 210), (160, 235), (200, 260)))
            rect2 = pygame.draw.polygon(screen, YELLOW, ((420, 210), (460, 235), (420, 260)))
            rect3 = pygame.draw.polygon(screen, YELLOW, ((200, 120), (160, 145), (200, 170)))
            rect4 = pygame.draw.polygon(screen, YELLOW, ((420, 120), (460, 145), (420, 170)))
            screen.blit(play, playRect)
            screen.blit(cancel,cancelRect)
            pygame.draw.rect(screen, WHITE, (120, 370, 160, 70), 4) #Next
            pygame.draw.rect(screen, WHITE, (340, 370, 160, 70), 4) #Continue
            pygame.draw.rect(screen, WHITE, (230, 450, 160, 70), 4) #Cancel 
            snake_list[cnt1].draw(screen)
            screen.blit(level[cnt2][0], level[cnt2][1])
        #----------------------------------------
        if playing == True:
            break
        
        if checkExit == 1:
            screen.blit(exit, (300, -50))
        pygame.display.update()
    if playing == True:
        #print("check continue", ctn_check)
        import game
        if ctn_check == 0:
            menu = game.playingGame(color_snake[cnt1][0], color_snake[cnt1][1], level[cnt2][2], level[cnt2][3], ctn_check, cnt2)
        else:
            last_lv = levelGame()
            #print(colorHead(), colorBody(), last_lv)
            menu = game.playingGame(colorHead(), colorBody(), level[last_lv][2], level[last_lv][3], ctn_check, cnt2)
        if menu == False:
            break