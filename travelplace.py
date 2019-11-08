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
  ##  button = pg.image.load('./Image/button.jpg')
  ##  button = (pg.transform.scale(button,(200,100))).convert_alpha()
   ## b = screen.blit(button,(300,200))

    #--------------------------------돈 출력--------------------------------------#
  ##  money_Font = pg.font.Font(None,30)
  ##  money_Text = money_Font.render("Money : " + str(money),True,black,white)
  ##  money_Textrect = money_Text.get_rect()
   ## money_Textrect.center = (50,400)
   ## screen.blit(money_Text,money_Textrect)

    #-----------------------------화면 출력 코드----------------------------------#
    ##pg.display.update()
    ##clock.tick(FPS)
  

  #--------------------------------여행지--------------------------------------#

  # 마우스 커서 위치 확인하는 코드
   # text = realtime_Font.render('cursor = '+str(pg.mouse.get_pos()),True,(0,100,0))
   # textrect = text.get_rect()
   # textrect.center =(100,100)
   # screen.blit(text,textrect)

    Map = pg.image.load('./Image/TravelMap.png')
    Map = (pg.transform.scale(Map,(800,600))).convert_alpha()
    Map_blit = screen.blit(Map,(-75,0))

    Space = pg.image.load('./Image/Space1.png')
    Space = (pg.transform.scale(Space,(300,400))).convert_alpha()
    Space_blit = screen.blit(Space,(550,80))

    Moon = pg.image.load('./Image/Moon.png')
    Moon = (pg.transform.scale(Moon,(130,100))).convert_alpha()
    Moon_blit = screen.blit(Moon,(660,185))

    Andromeda = pg.image.load('./Image/Galaxy.png')
    Andromeda = (pg.transform.scale(Andromeda,(170,185))).convert_alpha()
    Andromeda_blit = screen.blit(Andromeda,(650,255))


    Japan = pg.image.load('./Image/Pin.png')
    Japan = (pg.transform.scale((Japan),(100,50))).convert_alpha()
    Japan_blit = screen.blit(Japan,(461,216))

    Taiwan = pg.image.load('./Image/Pin.png')
    Taiwan = (pg.transform.scale((Taiwan),(100,50))).convert_alpha()
    Taiwan_blit= screen.blit(Taiwan,(438,249))

    Singapore = pg.image.load('./Image/Pin.png')
    Singapore = (pg.transform.scale((Singapore),(100,50))).convert_alpha()
    Singapore_blit = screen.blit(Singapore,(382,325))

    Russia = pg.image.load('./Image/Pin.png')
    Russia = (pg.transform.scale((Russia),(100,50))).convert_alpha()
    Russia_blit = screen.blit(Russia,(319,137))

    Austraila = pg.image.load('./Image/Pin.png')
    Austraila = (pg.transform.scale(Austraila,(100,50))).convert_alpha()
    Austraila_blit = screen.blit(Austraila,(501,427))

    Turkey = pg.image.load('./Image/Pin.png')
    Turkey = (pg.transform.scale(Turkey,(100,50))).convert_alpha()
    Turkey_blit = screen.blit(Turkey,(130,192))

    Italy = pg.image.load('./Image/Pin.png')
    Italy = (pg.transform.scale(Italy,(100,50))).convert_alpha()
    Italy_blit = screen.blit(Italy,(80,189))

    Switzerland = pg.image.load('./Image/Pin.png')
    Switzerland = (pg.transform.scale(Italy,(100,50))).convert_alpha()
    Switzerland_blit = screen.blit(Switzerland,(45,162))

    South_Pole = pg.image.load('./Image/Pin.png')
    South_Pole = (pg.transform.scale(South_Pole,(100,50))).convert_alpha()
    South_Pole_blit = screen.blit(South_Pole,(256,552))



    #----------------------------이벤트 발생 코드---------------------------------#
    for event in pg.event.get():
        
      ##  if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
       ##     pos = pg.mouse.get_pos()
       ##     if b.collidepoint(pos):
       ##         money += money_Add


        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    clock.tick(FPS)