#khai báo thư viện,...
import pygame, sys, math, random
from pyvidplayer import Video
pygame.font.init()
pygame.init()

# Khởi tạo giá trị, biến toàn cục
YELLOW = (236, 236, 50)
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
WHITE_1 = (230, 230, 230)
WHITE_B = (200, 200, 200)
GREEN_MONO = (0, 130, 0)
GREEN_DARK = (0, 90, 0)
GREEN_BRIGHT = (0, 230, 0)
BLACK = (0, 0, 0)
BLUE = (50, 100, 236)
RoyalBlue4 = (39, 64, 139)
RoyalBlue3 = (58, 95, 205)
MidnightBlue = (25, 25, 112)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
DarkOrchid4 = (104, 34, 139)
DarkOrchid1 = (191, 62, 255)
GRAY11 = (28, 28, 28)
GRAY22 = (22, 22, 22)
DarkSlateBlue = (72, 61, 139)
Dark_DarkSlateBlue = (31, 30, 70)
Cyan = (0, 200, 200)
Magenta1 = (255, 0, 255)
LightSeaGreen = (32, 178, 170)
Purple1 = (160, 32, 240)
Purple5	= (85, 26, 139)

screen = pygame.display.set_mode((600, 800))

cd = 100
running = True
gg = False 
bg_y = 0
image1 = True
image2 = False
image3 = False
image4 = False
last_click = -1000
bg = pygame.image.load(r'space-invaders-UI\bg.png')
icon = pygame.image.load(r'space-invaders-UI\OIP.jpg')
game_name = pygame.image.load(r'space-invaders-UI\Name.png')

# Điều kiện chạy GUI
menu = True 
tuto = False
credit = False  
panel = False
exit = False
LV1_start = False
LV2_start = False
Endless_1 = False
Endless_2 = False
#Permission
Unlock_EndlessMode = False
lv1_passed = False

# Intro trong quá trình thử nghiệm
# vid = Video(r'space-invaders-UI\Tic Tac Toe Video.mp4')
# vid.set_size((600, 800))
# def intro(): 
#     vid.draw(screen, (0, 0))
#     pygame.display.update()

# bảng score
def background():
    global bg_y
    bg_y -= 1 
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y + 800))
    if bg_y == -800:
        bg_y = 0

def reset_all():
    global panel, menu, tuto, credit, LV1_start, LV2_start, Endless_1, Endless_2
    tuto = menu = panel = credit = LV1_start = LV2_start = Endless_1 = Endless_2 = False 
def Exit():
    global exit
    global last_click
    key_pressed = pygame.key.get_pressed() 
    time_now = pygame.time.get_ticks()
    if key_pressed[pygame.K_ESCAPE] and time_now - last_click > cd:
        last_click = time_now   
        exit = not exit
    if exit:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        pygame.draw.rect(screen, GRAY11, (150, 300, 300, 150), 0, 8)
        pygame.draw.rect(screen, BLUE, (160, 310, 280, 130), 0, 8)
        pygame.draw.rect(screen, RED, (170, 390, 125, 40), 0, 8)
        pygame.draw.rect(screen, WHITE, (170, 330, 125, 40), 0, 8)
        pygame.draw.rect(screen, WHITE, (305, 330, 125, 40), 0, 8)
        pygame.draw.rect(screen, WHITE, (305, 390, 125, 40), 0, 8)
        if mouse_x >= 170 and mouse_x <= 170 + 125 and mouse_y >= 390 and mouse_y <= 390 + 40:
            pygame.draw.rect(screen, DARK_RED, (170, 390, 125, 40), 0, 8)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        global running
                        running = False
        if mouse_x >= 170 and mouse_x <= 170 + 125 and mouse_y >= 330 and mouse_y <= 330 + 40:
            pygame.draw.rect(screen, WHITE_B, (170, 330, 125, 40), 0, 8)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        exit = not exit
        if mouse_x >= 305 and mouse_x <= 305 + 125 and mouse_y >= 390 and mouse_y <= 390 + 40:
            pygame.draw.rect(screen, WHITE_B, (305, 390, 125, 40), 0, 8)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        reset_all()
                        global menu
                        menu = True 
        if mouse_x >= 305 and mouse_x <= 305 + 125 and mouse_y >= 330 and mouse_y <= 330 + 40:
            pygame.draw.rect(screen, WHITE_B, (305, 330, 125, 40), 0, 8)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        exit = not exit
                        # Khởi tạo lại dữ liệu LV.1 
        back_text = smallfont.render('Back', True, BLACK)
        restart_text = smallfont.render('Restart', True, BLACK)
        quit_text = smallfont.render('Quit', True, BLACK)
        menu_text = smallfont.render('Menu', True, BLACK)
        screen.blit(menu_text, (330, 385))
        screen.blit(quit_text, (200, 385))
        screen.blit(back_text, (200, 330))
        screen.blit(restart_text, (315, 330)) 
def Score(score):
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    pygame.draw.rect(screen, MidnightBlue, (350, -10, 300, 70), 0, 12)
    pygame.draw.rect(screen, RoyalBlue3, (360, -10, 300, 61), 0, 12)
    text_score = smallfont.render("Score: " + str(score), True, WHITE)
    screen.blit(text_score, (400, 8))

def Hp(hp):
    Heart = pygame.image.load(r'space-invaders-UI/Heart.png')
    pygame.draw.rect(screen, MidnightBlue, (-50, 740, 330, 150), 0, 12)
    pygame.draw.rect(screen, RoyalBlue3, (-50, 750, 320, 150), 0, 12)
    if hp > 0:
        screen.blit(Heart, (25, 755))
    if hp > 1:
        screen.blit(Heart, (100, 755))
    if hp > 2:
        screen.blit(Heart, (175, 755))

def Rocket(rocket):
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    Rocket = pygame.image.load(r'space-invaders-UI/rocket.png')
    pygame.draw.rect(screen, MidnightBlue, (480, 740, 330, 150), 0, 12)
    pygame.draw.rect(screen, RoyalBlue3, (490, 750, 320, 150), 0, 12)
    screen.blit(Rocket, (495, 753))
    slrocket = smallfont.render(str(rocket), True, BLACK)
    screen.blit(slrocket, (540, 755))

def LV1_starting():
    reset_all()
    background()
    global LV1_start
    LV1_start = True
    Score(111)
    Hp(3)
    Rocket(3)
    Exit()

def LV2_starting():
    pass
def EL_1P():
    pass
def EL_2P():
    pass

# tên game + icon game
def Name():
    icon = pygame.image.load(r'space-invaders-UI\OIP.jpg')
    pygame.display.set_icon(icon)
    GAMENAME = 'Space Campaign'
    pygame.display.set_caption(GAMENAME)
def Menu():
    background()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(game_name, (75, 50))
    smallfont = pygame.font.SysFont('Comic Sans MS', 30)
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text_play = font.render('Play', True, BLACK)
    text_help = font.render('Tutorial', True, BLACK)
    text_quit = font.render('QUIT', True, BLACK)
    text_credit = smallfont.render('Credit', True, WHITE)
    pygame.draw.rect(screen, GRAY11, (0, 0, 600, 800), 10)
    pygame.draw.rect(screen, WHITE, (160, 460, 280, 60), 0, 10)
    pygame.draw.rect(screen, GREEN_MONO, (160, 570, 280, 60), 0, 10)
    pygame.draw.rect(screen, RED, (160, 680, 280, 60), 0, 8)
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 680 and mouse_y <= 680 + 60:
        pygame.draw.rect(screen, DARK_RED, (160, 680, 280, 60), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                global running
                running = False
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 460 and mouse_y <= 460 + 60:
        pygame.draw.rect(screen, WHITE_B, (160, 460, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global panel
                    panel = True
    if mouse_x <= 160 + 280 and mouse_x >= 160 and mouse_y >= 570 and mouse_y <= 570 + 60:
        pygame.draw.rect(screen, GREEN_DARK, (160, 570, 280, 60), 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    global tuto
                    tuto = True
    if mouse_x <= 98 and mouse_x >= 10 and mouse_y >= 760 and mouse_y <= 785: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global credit
                    credit = not credit  
    screen.blit(text_play, (255, 450))
    screen.blit(text_help, (205, 560))
    screen.blit(text_quit, (230, 670))
    screen.blit(text_credit,(10, 750))
def Credit():
    font = pygame.font.SysFont('Comic Sans MS', 40)
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    pygame.draw.rect(screen, GRAY11, (60, 150, 480, 300), 0, 8)
    pygame.draw.rect(screen, WHITE, (70, 160, 460, 280), 0, 8)
    text_0 = font.render('Credit', True, BLACK)
    text_1 = smallfont.render('Quang: Game designer, UI designer', True, BLACK)
    text_2 = smallfont.render('Nga: Artist, Marketing', True, BLACK)
    text_3 = smallfont.render('Hung Thinh: Programmer', True, BLACK)
    text_4 = smallfont.render('Huy Thinh: Programmer', True, BLACK)
    screen.blit(text_0, (240, 150))
    screen.blit(text_1, (80, 210))
    screen.blit(text_2, (80, 260))
    screen.blit(text_3, (80, 310))
    screen.blit(text_4, (80, 360))
def Panel():
    lock = pygame.image.load(r'space-invaders-UI\lock.png')
    biglock = pygame.transform.scale(lock, (200, 272))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    smallfont = pygame.font.SysFont(None, 30)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    global panel
    background()
    pygame.draw.rect(screen, Purple5, (100, 100, 400, 600), 0, 8)
    pygame.draw.rect(screen, DarkSlateBlue, (105, 105, 390, 590), 0, 8)
    pygame.draw.line(screen, BLACK, (105, 300), (494, 300), 5)
    pygame.draw.rect(screen, DarkOrchid1, (125, 175, 160, 55), 0, 8)
    pygame.draw.rect(screen, DarkOrchid1, (315, 175, 160, 55), 0, 8)
    pygame.draw.rect(screen, DarkOrchid1, (135, 400, 250, 55), 0, 8)
    pygame.draw.rect(screen, DarkOrchid1, (135, 550, 250, 55), 0, 8)
    pygame.draw.rect(screen, WHITE, (0, 0, 100, 100), 0, 8)
    if mouse_x <= 100 and mouse_x >= 0 and mouse_y >= 0 and mouse_y <= 100:
        pygame.draw.rect(screen, WHITE_B, (0, 0, 100, 100), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    panel = False
    pygame.draw.polygon(screen, BLACK,[[50, 15], [50, 85], [5, 50]])
    pygame.draw.rect(screen, BLACK, (50, 30, 40, 40))
    if mouse_x <= 125 + 160 and mouse_x >= 125 and mouse_y >= 175 and mouse_y <= 175 + 55:
        pygame.draw.rect(screen, DarkOrchid4, (125, 175, 160, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global lv1_passed 
                    lv1_passed = True
                    global LV1_start
                    LV1_start = True 
    if mouse_x <= 315 + 160 and mouse_x >= 315 and mouse_y >= 175 and mouse_y <= 175 + 55 and lv1_passed:
        pygame.draw.rect(screen, DarkOrchid4, (315, 175, 160, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Unlock_EndlessMode
                    Unlock_EndlessMode = True
                    global LV2_start
                    LV2_start = True 
    if mouse_x <= 135 + 250 and mouse_x >= 135 and mouse_y >= 400 and mouse_y <= 400 + 55 and Unlock_EndlessMode:
        pygame.draw.rect(screen, DarkOrchid4, (135, 400, 250, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Endless_1
                    Endless_1 = True
    if mouse_x <= 135 + 250 and mouse_x >= 135 and mouse_y >= 550 and mouse_y <= 550 + 55 and Unlock_EndlessMode:
        pygame.draw.rect(screen, DarkOrchid4, (135, 550, 250, 55), 0, 8)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    global Endless_2
                    Endless_2 = True
    Ordinary_Mode_text = font.render('Ordinary Mode', True, Magenta1)
    Endless_Mode_text = font.render('Endless Mode', True, Magenta1)
    Lv1_text = font.render('Level 1', True, BLACK)
    Lv2_text = font.render('Level 2', True, BLACK)
    One_player_mode_text = font.render('1-player mode', True, BLACK)
    Two_player_mode_text = font.render('2-player mode', True, BLACK)
    text_0_1 = smallfont.render('Complete all levels in Ordinary Mode', True, BLACK)
    text_0_2 = smallfont.render('to unlock Endless Mode', True, BLACK)
    text_1 = smallfont.render('Playing alone is still good', True, BLACK)
    text_2 = smallfont.render('Playing with friend is fun? Right?', True, BLACK)
    if lv1_passed == False: 
        screen.blit(lock, (375, 175))
    if Unlock_EndlessMode == False:
        screen.blit(lock, (250, 400))
        screen.blit(lock, (250, 550))
    screen.blit(Ordinary_Mode_text, (180, 110))
    screen.blit(Lv1_text, (150, 180))
    screen.blit(Lv2_text, (335, 180))
    screen.blit(text_0_1, (120, 250))
    screen.blit(text_0_2, (120, 280))
    screen.blit(Endless_Mode_text, (190, 300))
    screen.blit(One_player_mode_text, (150, 400))
    screen.blit(Two_player_mode_text, (150, 550))
    screen.blit(text_1, (150, 470))
    screen.blit(text_2, (150, 620))
# Mục Tutorial
def Tutorial():
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    font = pygame.font.SysFont('Comic Sans MS', 35)
    smallfont = pygame.font.SysFont('Comic Sans MS', 25)
    small1font = pygame.font.SysFont('Comic Sans MS', 20)
    background()
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
    pygame.draw.rect(screen, WHITE, (180, 600, 65, 65), 0, 8)
    pygame.draw.rect(screen, WHITE, (350, 600, 65, 65), 0, 8)
    pygame.draw.polygon(screen, BLACK, [[235, 603], [235, 660], [185, 635]])
    pygame.draw.polygon(screen, BLACK,[[360, 603], [360, 660], [410, 635]])
    time_now = pygame.time.get_ticks()
    global last_click
    if mouse_x <= 180 + 65 and mouse_x >= 180 and mouse_y >= 600 and mouse_y <= 600 + 65:
        pygame.draw.rect(screen, WHITE_B, (180, 600, 65, 65), 0, 8)
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
        pygame.draw.rect(screen, WHITE_B, (350, 600, 65, 65), 0, 8)
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
        image_1 = smallfont.render('[Image of Gameplay]', True, WHITE)
        text_1_1 = smallfont.render('The aliens are coming! Your mission is to', True, WHITE)
        text_1_2 = smallfont.render('prevent their descent and invasion by', True, WHITE)
        text_1_3 = smallfont.render('shooting them down.', True, RED)
        screen.blit(image_1, (60, 150))
        screen.blit(text_1_1, (70, 450))
        screen.blit(text_1_2, (80, 480))
        screen.blit(text_1_3, (190, 510))
    elif image2:
        list_2 = smallfont.render('2/4', True, WHITE)
        screen.blit(list_2, (278, 610))
        image_2 = smallfont.render('[Image of Gameplay]', True, WHITE)
        text_2_1 = small1font.render('Eliminate the aliens to get much scores as you can!', True, GREEN_MONO)
        text_2_2 = smallfont.render('Careful! Aliens will shoot back at you.', True, WHITE)
        text_2_3 = smallfont.render('You only have 3 lives!', True, WHITE)
        screen.blit(image_2, (60, 150))
        screen.blit(text_2_1, (68, 465))
        screen.blit(text_2_2, (85, 485))
        screen.blit(text_2_3, (170, 510))
    elif image3:
        list_3 = smallfont.render('3/4', True, WHITE)
        screen.blit(list_3, (278, 610))
        text_3_1_0 = font.render('In one-player mode:', True, BLACK)
        text_3_1_1 = smallfont.render('- USE WASD to move spaceships', True, GREEN_MONO)
        text_3_1_2 = smallfont.render('- Click left mouse to shoot.', True, GREEN_MONO)
        text_3_1_3 = smallfont.render('- Click right mouse to launch rockets.', True, GREEN_MONO)
        text_3_2_0 = font.render('In two-player mode:', True, BLACK)
        text_3_1_1_0 = smallfont.render('- Player 1: ', True, GREEN_MONO)
        text_3_1_1_1 = smallfont.render('+ Move: WASD', True, GREEN_MONO)
        text_3_1_1_2 = smallfont.render('+ Shoot: "F"', True, GREEN_MONO)
        text_3_1_1_3 = smallfont.render('+ launch rockets: "G"', True, GREEN_MONO)
        text_3_1_2_0 = smallfont.render('- Player 2:', True, GREEN_MONO)
        text_3_1_2_1 = smallfont.render('+ Move: Arrow keys', True, GREEN_MONO)
        text_3_1_2_2 = smallfont.render('+ Shoot: "0"', True, GREEN_MONO)
        text_3_1_2_3 = smallfont.render('+ launch rockets: "1"', True, GREEN_MONO)
        screen.blit(text_3_1_0, (70, 160))
        screen.blit(text_3_1_1, (90, 210))
        screen.blit(text_3_1_2, (90, 235))
        screen.blit(text_3_1_3, (90, 260))
        screen.blit(text_3_2_0, (70, 290))
        screen.blit(text_3_1_1_0, (90, 335))
        screen.blit(text_3_1_1_1, (110, 365))
        screen.blit(text_3_1_1_2, (110, 390))
        screen.blit(text_3_1_1_3, (110, 415))
        screen.blit(text_3_1_2_0, (90, 440))
        screen.blit(text_3_1_2_1, (110, 465))
        screen.blit(text_3_1_2_2, (110, 490))
        screen.blit(text_3_1_2_3, (110, 515))
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
    if menu:
        Menu()
    if credit:
        Credit()
    if tuto:
        Tutorial()
    if panel:
        Panel()
    if LV1_start:
        LV1_starting()
    if LV2_start:
        LV2_starting()
    if Endless_1:
        EL_1P()
    if Endless_2:
        EL_2P()

while running:
    GUI()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
