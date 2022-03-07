import sys, pygame
import time
pygame.init()

width, height = 640, 480
size=(width, height)
speed = [0, 0]
black = (0, 0, 0)
tastoPremuto = ''
screen = pygame.display.set_mode(size)

ball = pygame.image.load("img/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            tastoPremuto = event.__dict__["unicode"]
            print(tastoPremuto)
        if tastoPremuto == "w":
            if ballrect.top < 0:
                speed = [0,0]
            else:speed=[0,-1]
        if tastoPremuto == "a":
            if ballrect.left < 0:
                speed = [0,0]
            else: speed=[-1,0]
        if tastoPremuto == "s":
            if ballrect.right > width:
                speed = [0,0]
            else: speed=[0,1]
        if tastoPremuto == "d":
            if ballrect.bottom > height:
                speed = [0,0]
            else: speed=[1,0]
    
    ballrect = ballrect.move(speed)
    speed = [0,0]


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()