#khai báo thư viện,...
import pygame, sys, math, random
from pyvidplayer import Video
pygame.font.init()
pygame.init()

# Khởi tạo giá trị, biến toàn cục
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
WHITE_1 = (230, 230, 230)
WHITE_B = (200, 200, 200)
GREEN_MONO = (0, 130, 0)
GREEN_DARK = (0, 90, 0)
GREEN_BRIGHT = (0, 230, 0)
BLACK = (0, 0, 0)
RoyalBlue4 = (39, 64, 139)
RoyalBlue3 = (58, 95, 205)
MidnightBlue = (25, 25, 112)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
DarkOrchid4 = (104, 34, 139)
GRAY11 = (28, 28, 28)
GRAY22 = (22, 22, 22)
screen = pygame.display.set_mode((600, 800))
tuto = False
score = 0
bg_y = 0
image1 = True
image2 = False
image3 = False
image4 = False
last_click = -1000
bg = pygame.image.load(r'space-invaders-UI\bg.png')
icon = pygame.image.load(r'space-invaders-UI\OIP.jpg')
game_name = pygame.image.load(r'space-invaders-UI\Name.png')

# Intro trong quá trình thử nghiệm
# vid = Video(r'space-invaders-UI\Tic Tac Toe Video.mp4')
# vid.set_size((600, 800))
# def intro(): 
#     vid.draw(screen, (0, 0))
#     pygame.display.update()

# tên game + icon game
def Name():
    icon = pygame.image.load(r'space-invaders-UI\OIP.jpg')
    pygame.display.set_icon(icon)
    GAMENAME = 'Space Campaign'
    pygame.display.set_caption(GAMENAME)
def Menu():
    global bg_y
    bg_y -= 1 
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y + 800))
    if bg_y == -800:
        bg_y = 0
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(game_name, (75, 50))
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text_play = font.render('Play', True, BLACK)
    text_help = font.render('Tutorial', True, BLACK)
    pygame.draw.rect(screen, GRAY11, (0, 0, 600, 800), 10)
    pygame.draw.rect(screen, WHITE, (160, 460, 280, 60), 0, 10)
    pygame.draw.rect(screen, GREEN_MONO, (160, 570, 280, 60), 0, 10)
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 460 and mouse_y <= 460 + 60:
        pygame.draw.rect(screen, WHITE_B, (160, 460, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pass
                    # PLAYING THE GAME
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 570 and mouse_y <= 570 + 60:
        pygame.draw.rect(screen, GREEN_DARK, (160, 570, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    global tuto
                    tuto = True
    screen.blit(text_play, (255, 450))
    screen.blit(text_help, (210, 560))
running = True
# bảng score
def score(score):
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    pygame.draw.rect(screen, MidnightBlue, (350, -10, 300, 70), 0, 12)
    pygame.draw.rect(screen, RoyalBlue3, (360, -10, 300, 61), 0, 12)
    text_score = smallfont.render("Score: " + str(score), True, BLACK)
    screen.blit(text_score, (400, 8))
def HPandRocket(hp, rocket):
    pass
# Mục Tutorial
def Tutorial():
    cd = 100
    mouse_x, mouse_y = pygame.mouse.get_pos()
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    small2font = pygame.font.SysFont('Comic Sans MS', 24)
    small1font = pygame.font.SysFont('Comic Sans MS', 20)
    global bg_y
    bg_y -= 1 
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y + 800))
    if bg_y == -800:
        bg_y = 0
    pygame.draw.rect(screen, GRAY11, (0, 0, 600, 800), 10)
    pygame.draw.rect(screen, RED, (525, 0, 75, 75))
    if mouse_x <= 525 + 75 and mouse_x >= 525 and mouse_y >= 0 and mouse_y <= 75:
        pygame.draw.rect(screen, DARK_RED, (525, 0, 75, 75))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    global tuto
                    tuto = False
    global image1, image2, image3, image4
    pygame.draw.line(screen, BLACK, (533, 5), (590, 70), 8)
    pygame.draw.line(screen, BLACK, (533, 70), (590, 5), 8)
    pygame.draw.rect(screen, WHITE_B, (60, 150, 480, 450), 0, 8)
    pygame.draw.rect(screen, WHITE, (180, 600, 65, 65))
    pygame.draw.rect(screen, WHITE, (350, 600, 65, 65))
    pygame.draw.polygon(screen, BLACK, [[235, 603], [235, 660], [185, 635]])
    pygame.draw.polygon(screen, BLACK,[[360, 603], [360, 660], [410, 635]])
    time_now = pygame.time.get_ticks()
    global last_click
    if mouse_x <= 180 + 65 and mouse_x >= 180 and mouse_y >= 600 and mouse_y <= 600 + 65:
        pygame.draw.rect(screen, WHITE_B, (180, 600, 65, 65))
        pygame.draw.polygon(screen, GRAY11, [[235, 603], [235, 660], [185, 635]])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and time_now - last_click > cd:
                    last_click = time_now
                    if image4:
                        image3 = True
                        image4 = False
                    elif image3:
                        image2 = True
                        image3 = False
                    elif image2:
                        image1 = True
                        image2 = False
    if mouse_x <= 350 + 65 and mouse_x >= 350 and mouse_y >= 600 and mouse_y <= 600 + 65:
        pygame.draw.rect(screen, WHITE_B, (350, 600, 65, 65))
        pygame.draw.polygon(screen, GRAY11,[[360, 603], [360, 660], [410, 635]])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and time_now - last_click > cd:
                    last_click = time_now
                    if image3:
                        image3 = False
                        image4 = True
                    elif image2:
                        image2 = False
                        image3 = True
                    elif image1:
                        image1 = False
                        image2 = True
    if image1:
        list_1 = smallfont.render('1/4', True, WHITE)
        screen.blit(list_1, (278, 610))
        text_1_1 = smallfont.render('The aliens are coming! Your mission is to', True, WHITE)
        text_1_2 = smallfont.render('prevent their descent and invasion by', True, WHITE)
        text_1_3 = smallfont.render('shooting them down.', True, RED)
        screen.blit(text_1_1, (70, 450))
        screen.blit(text_1_2, (80, 480))
        screen.blit(text_1_3, (190, 510))
    elif image2:
        list_2 = smallfont.render('2/4', True, WHITE)
        screen.blit(list_2, (278, 610))
        text_2_1 = small1font.render('Eliminate the aliens to get much scores as you can!', True, GREEN_MONO)
        text_2_2 = smallfont.render('Careful! Aliens will shoot back at you.', True, WHITE)
        text_2_3 = smallfont.render('You only have 3 lives!', True, WHITE)
        screen.blit(text_2_1, (68, 465))
        screen.blit(text_2_2, (85, 485))
        screen.blit(text_2_3, (170, 510))
    elif image3:
        list_3 = smallfont.render('3/4', True, WHITE)
        screen.blit(list_3, (278, 610))
        text_2_1 = small2font.render('Use the keyboard to move your spaceship.', True, GREEN_MONO)
        text_2_2 = smallfont.render('Click left mouse to shoot.', True, GREEN_MONO)
        text_2_3 = smallfont.render('Click right mouse to launch rockets.', True, GREEN_MONO)
        screen.blit(text_2_1, (68, 460))
        screen.blit(text_2_2, (70, 485))
        screen.blit(text_2_3, (70, 510))
    elif image4:
        Red_present = pygame.image.load(r'space-invaders-UI\Red_present-removebg.png') 
        list_4 = smallfont.render('4/4', True, WHITE)
        screen.blit(list_4, (278, 610))
        screen.blit(Red_present, (200, 250))
        text_4_1 = smallfont.render('Look out for gift box power-ups that', True, WHITE)
        text_4_2 = smallfont.render('make you more powerful', True, WHITE)
        text_4_3 = smallfont.render('Have a great time!', True, RoyalBlue4)
        screen.blit(text_4_1, (85, 450))
        screen.blit(text_4_2, (160, 475))
        screen.blit(text_4_3, (190, 525))
def GUI():
    Name()
    if tuto == False:
        Menu()
    else:
        Tutorial()
while running:
    GUI()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()