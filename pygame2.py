import pygame
import time

pygame.init()
# to display colors
# gw-game_width #gh-game_geight
dist = 25
gw = 800
gh = 600
gamewindow = pygame.display.set_mode((gw, gh))
pygame.display.set_caption('Snake Game')
pygame.display.update()
font = pygame.font.SysFont(None, 100)


def message_to_screen(msg, color):
    gw = 800
    gh = 600
    gamewindow = pygame.display.set_mode((gw, gh))
    screen_text = font.render(msg, True, color)
    gamewindow.blit(screen_text, [0, 0])


img = pygame.image.load('72269.3.jpg').convert()
clk = pygame.time.Clock()


def loop():
    gw = 800
    gh = 600
    gamewindow = pygame.display.set_mode((gw, gh))
    gameclose = False
    gameover = True
    start_x = gw / 2
    start_y = gh / 2
    update_x = 0
    update_y = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    d = (78, 56, 34)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    # gw-game_width #gh-game_geight
    dist = 25
    while not gameclose:
        while not gameover:
            gamewindow.fill(white)
            message_to_screen("YOU LOSE!!! ,Press 'r' to replay OR press 'q' to quit", red)
            pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameclose = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    loop()
                if e.key == pygame.K_q:
                    gamewindow = True
        for e in pygame.event.get():
            if e.key == pygame.K_LEFT:
                update_x = -dist
            if e.key == pygame.K_RIGHT:
                update_x = +dist
            if e.key == pygame.K_UP:
                update_y = -dist
            if e.key == pygame.K_DOWN:
                update_y = +dist
        for e in pygame.event.get():
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or pygame.K_DOWN or pygame.K_LEFT or pygame.K_RIGHT:
                    update_x = 0
                    update_y = 0
        # to fill background colour--
        start_x += update_x
        start_y += update_y
        if start_y <= 0:
            gameclose = True
        if start_y >= gh:
            gameclose = True
        if start_x == 0:
            gameclose = True
        if start_x >= gw:
            gameclose = True
        clk.tick(12)
        gamewindow.fill((25, 255, 100))
        # to set background image
        # gamewindow.blit(img,[0,0])
        # to draw line--pygame.draw.line(gamewindow,(18,90,170),[0,0],[50,30],5)
        # pygame.draw.rect(gamewindow,red,[75,10,dist,24])
        # pygame.draw.polygon(gamewindow,(34,dist4,89),[[100,88],[56,78],[67,34]])
        # pygame.draw.circle(gamewindow,red,[400,300],100)
        pygame.draw.rect(gamewindow, red, [start_x, start_y, 30, 30])
        pygame.display.update()
        # for automatic screen close within 5 sec -time.sleep(5)
    pygame.quit()
    quit()
loop()