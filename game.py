import pygame, numpy as np, setting
from character import Snake
from character import Fruit
from setting import movingSound, eatingSound, winnerSound, mouseClickSound, crashSound
from setting import pause_icon, pause_icon_rect, pause_screen, exit
from color import RED, WHITE, BLACK, GREY, BLACKK
import continueGame

#-----------------------------------------
wScreen, hScreen = 600, 600
gameover = pygame.image.load('Picture/SnakeGameOver.png')
gameover = pygame.transform.scale(gameover, (600, 600))
level = [[6, 1], [8, 50], [10, 60]]
#-----------------------------------------
#------------Text------------------------
font = pygame.font.Font('freesansbold.ttf', 32)

play = font.render('Play again', True, WHITE)
playRect = play.get_rect(center = (305, 405))

cancel = font.render('Home', True, WHITE)
cancelRect = cancel.get_rect(center = (305, 485))
#--------------------------------------------
def displayBoard(screen, boardColor, color1, color2):
    for i in range(60, setting.screen_height - 60 + 1, setting.cell_size):
        x1, y1 = 60, i
        x2, y2 = setting.screen_width - 60, i
        pygame.draw.line(screen, boardColor, (x1, y1), (x2, y2), 1)
    for i in range(60, setting.screen_width - 60 + 1, setting.cell_size):
        x1, y1 = i, 60
        x2, y2 = i, setting.screen_height - 60
        pygame.draw.line(screen, boardColor, (x1, y1), (x2, y2), 1)
    state = False
    for i in range(60, setting.screen_height - 60 + 1, setting.cell_size):
        for j in range(60, setting.screen_width - 60 + 1, setting.cell_size):
            boardRect = pygame.Rect(i,j,setting.cell_size,setting.cell_size)
            state = 1 - state
            if state:
                pygame.draw.rect(screen, color1, boardRect)
            else:
                pygame.draw.rect(screen, color2, boardRect)
                
# def collision(Head, fruit):
#     for item in fruit:
#         if Head[0] == item[0] and Head[1] == item[1]:
#             fruit.remove(item)
#             return True
#     return False

def inside(pos, rect):
    return rect[0] <= pos[0] and pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] and pos[1] <= rect[1] + rect[3]

def saveGame(head, body, snake, fruit, lv):
    with open('Data/check.txt', 'w') as file:
        file.write(str(1))
    with open('Data/colorHead.txt', 'w') as file:
        file.write(str(head))
    with open('Data/colorBody.txt', 'w') as file:
        file.write(str(body))
    with open('Data/snake.txt', 'w') as file:
        file.write(str(snake.list))
    with open('Data/fruit.txt', 'w') as file:
        file.write(str(fruit.fruit))
    with open('Data/direction.txt', 'w') as file:
        file.write(str(snake.dir))
    with open('Data/level.txt', 'w') as file:
        file.write(str(lv))
#-------------------------------------------------------
clock = pygame.time.Clock()
def playingGame(head, body, fps = 5, numFruits = 30, ctn_check = 0, lv = 0):
    running = True
    gameActive = True
    stop = False
    winGame = False
    screen = pygame.display.set_mode((wScreen, hScreen))
    snake = Snake(colorHead=head, colorBody=body)
    fruit = Fruit(numberOfFruits = numFruits)
    
    if ctn_check == 1:
        stop = True
        snake.colorHead = continueGame.colorHead()
        snake.colorBody = continueGame.colorBody()
        snake.list = continueGame.snakeArray()
        snake.dir = continueGame.snakeDir()
        fruit.fruit = continueGame.foodArray()
        #print(snake.list)
        #snake.moved = 1
    
    checkExit = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running = False
                checkExit = 1
                #stop = True
                saveGame(head, body, snake, fruit, lv)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if checkExit == 1:
                        if inside(event.pos, (310, 45, 135, 35)):
                            running = False
                        if inside(event.pos, (455, 45, 135, 35)):
                            checkExit = 0    
                            #stop = 0
                    if stop == True and checkExit == False:
                        if circle2.collidepoint(event.pos):
                            stop = False
                        if circle1.collidepoint(event.pos):
                            saveGame(head, body, snake, fruit, lv)
                            return True
                    if gameActive == False:
                        if winGame == True:
                            with open('Data/check.txt', 'w') as file:
                                file.write(str(0))
                            if inside(event.pos, (220, 370, 170, 70)):
                                snake = Snake(head, body)
                                fruit = Fruit(numFruits)  
                                mouseClickSound.play()
                                gameActive = True
                                winGame = False
                            elif inside(event.pos, (220, 450, 170, 70)):
                                mouseClickSound.play()
                                return True
                        else:
                            if inside(event.pos, (105, 495, 95, 55)):
                                with open('Data/check.txt', 'w') as file:
                                    file.write(str(0))
                                return True
                            if inside(event.pos, (395, 495, 95, 55)):
                                snake = Snake(head, body)
                                fruit = Fruit(numFruits)  
                                mouseClickSound.play()
                                gameActive = True
                    if gameActive == True and pause_icon_rect.collidepoint(event.pos) and stop == False:
                        stop = True
                        saveGame(head, body, snake, fruit, lv)
            if event.type == pygame.KEYDOWN and gameActive:
                if event.key == pygame.K_UP:
                    movingSound.play()
                    snake.changeDir(0)
                if event.key == pygame.K_DOWN:
                    movingSound.play()
                    snake.changeDir(1)
                if event.key == pygame.K_LEFT:
                    movingSound.play()
                    snake.changeDir(2)
                if event.key == pygame.K_RIGHT:
                    movingSound.play()
                    snake.changeDir(3)
                if event.key == pygame.K_SPACE and checkExit == False:
                    if stop == False:
                        stop = True
                        saveGame(head, body, snake, fruit, lv)
                    else:
                        stop = False


        screen.fill('BLACK')
        screen.blit(pause_icon, pause_icon_rect)
        displayBoard(screen, WHITE, BLACKK, GREY)
        if stop == False and checkExit == False:
            snake.move()
        fruit.showFruit(screen)
        snake.draw(screen)
        
        if checkExit == 1:
            screen.blit(exit, (300, -50))
        if stop == True:
            circle1 = pygame.draw.circle(screen, WHITE, (245, 340), 41, width=0)
            circle2 = pygame.draw.circle(screen, WHITE, (391, 340), 41, width=1)
            screen.blit(pause_screen, (130, 200))
            pygame.display.update()
            continue
        
        #----------------win game---------------------
        if len(fruit.fruit) == 1:
            winGame = True
            if gameActive == True:
                winnerSound.play()
                gameActive = False
            screen.blit(setting.winnerImg,(0, -40))
            screen.blit(play, playRect)
            screen.blit(cancel, cancelRect)
            pygame.draw.rect(screen, WHITE, (220, 450, 170, 70), 4) #Home
            pygame.draw.rect(screen, WHITE, (220, 370, 170, 70), 4) #play again
            pygame.display.update()
            continue
        #--------------------------------------------
        [tailX,tailY] = [snake.list[len(snake.list)-1][0], snake.list[len(snake.list)-1][1]]
        
        # snake.move()
        # snake.draw(screen)
        if fruit.collision(snake.list[0]):
            eatingSound.play()
            snake.list = np.append(snake.list, [[tailX,tailY]], axis = 0)
            
        # fruit.showFruit(screen)
        
        if snake.gameOver() == True:
            if gameActive: 
                crashSound.play()
                pygame.time.delay(200)
            gameActive = False

        if gameActive == False:            
            screen.blit(gameover, (0, 0))
            if checkExit == 1:
                screen.blit(exit, (300, -50))

        pygame.display.update()
        clock.tick(fps)
    saveGame(head, body, snake, fruit, lv)
    return False