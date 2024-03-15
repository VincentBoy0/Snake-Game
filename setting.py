import pygame
from pygame import mixer
from color import BLACK, BLUE, YELLOW, GREEN, GREY, PINK, MINT, WHITE, RED
pygame.mixer.pre_init(44100,-16,2,512)
pygame.mixer.init()
#Display
screen_width = 600
screen_height = 600
cell_size = 20

#Fruit
numberOfFruits = 100
colorFruit = GREEN

#Initilize Img
background_intro = pygame.image.load('Picture/background_intro.jpg')
background_intro = pygame.transform.scale(background_intro, (800,600))
iconImg = pygame.image.load('Picture/snake.png')
winnerImg = pygame.image.load('Picture/win.jpg')
winnerImg = pygame.transform.scale(winnerImg, (600,600))
pause_icon = pygame.image.load('Picture/pause_icon.jpg')
pause_icon = pygame.transform.scale(pause_icon, (30, 30))
pause_icon_rect = pause_icon.get_rect(center = (550, 30))
pause_screen = pygame.image.load('Picture/pause_screen.png')
exit = pygame.image.load('Picture/exit.jpg')
exit = pygame.transform.scale(exit, (300, 140))
#Initilize Sound
movingSound = mixer.Sound('Sound/moving.wav')
movingSound.set_volume(0.1)
eatingSound = mixer.Sound('Sound/eating.wav')
gameOverSound = mixer.Sound('Sound/gameOver.flac')
winnerSound = mixer.Sound('Sound/winner.ogg')
mouseClickSound = mixer.Sound('Sound/mouseClick.wav')
crashSound = mixer.Sound('Sound/crash.mp3')
crashSound.set_volume(0.1)

