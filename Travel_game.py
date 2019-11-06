import pygame as pg
import time
import random
import datetime
import sys

#class travel

#class character

#class work

#class 

#--------------------------------게임 사전 설정-----------------------------------#
pg.init()
screen_width = 800
screen_height = 600
size = [screen_width, screen_height]
FPS = 60
white = (255,255,255)
black = (0,0,0)
screen = pg.display.set_mode(size) # 창크기 설정
pg.display.set_caption("가제 : 방구석 여ㅡ행")
clock = pg.time.Clock()
money = 0
money_Add = 100

while True:
    screen.fill(white)
    #----------------------------실시간 시간 출력---------------------------------#

    date = (datetime.datetime.now()).strftime("%Y / %m / %d / %H : %M : %S")
    realtime_Font = pg.font.Font(None, 25)
    realtime_Text = realtime_Font.render("Time : " + date,True,black,white)
    realtime_Textrect = realtime_Text.get_rect()
    realtime_Textrect.center = (660,30)
    screen.blit(realtime_Text,realtime_Textrect)

    #---------------------------버튼 생성 코드(예시)-------------------------------#
    button = pg.image.load('./Image/button.jpg')
    button = (pg.transform.scale(button,(200,100))).convert_alpha()
    b = screen.blit(button,(300,200))

    #--------------------------------돈 출력--------------------------------------#
    money_Font = pg.font.Font(None,30)
    money_Text = money_Font.render("Money : " + str(money),True,black,white)
    money_Textrect = money_Text.get_rect()
    money_Textrect.center = (50,400)
    screen.blit(money_Text,money_Textrect)

    #-----------------------------화면 출력 코드----------------------------------#
    ##pg.display.update()
    ##clock.tick(FPS)
  
    #----------------------------이벤트 발생 코드---------------------------------#
    for event in pg.event.get():
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if b.collidepoint(pos):
                money += money_Add


        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    clock.tick(FPS)