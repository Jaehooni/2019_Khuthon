import pygame as pg
import time
import random
import datetime

"""
class button:
    place = " "
    place_list = [main,[travel_1,travel_2],[work_1,work_2,work_3],mini_game,status]
    image_link = " "
    def __init__(_self_):
        place = place_list[0]
        image_link = './Image/money_button.jpg'

    def __init__(_self_,_place,_image_link):
        place = _place
        image_link = _image_link

    def getPlace():
        return place

    def getImagelink():
        return image_link
"""


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
Screen = 0 # screen이 0, 1 ,2 ,3 ,4 ,5 일때 다른 화면 설정

while True:
    if (Screen == 0):
        screen.fill(white)
        #----------------------------실시간 시간 출력---------------------------------#
        date = (datetime.datetime.now()).strftime("%Y / %m / %d / %H : %M : %S")
        realtime_Font = pg.font.Font(None, 25)
        realtime_Text = realtime_Font.render("Time : " + date,True,black,white)
        realtime_Textrect = realtime_Text.get_rect()
        realtime_Textrect.center = (660,30)
        screen.blit(realtime_Text,realtime_Textrect)

        #----------------------------돈 버튼 생성 코드---------------------------------#
        money_button = pg.image.load('./Image/money_button.jpg')
        money_button = (pg.transform.scale(money_button,(100,100))).convert_alpha()
        money_b = screen.blit(money_button,(50,500))

        #---------------------------여행 버튼 생성 코드--------------------------------#
        travel_button = pg.image.load('./Image/travel_button.jpg')
        travel_button = (pg.transform.scale(travel_button,(100,100))).convert_alpha()
        travel_b = screen.blit(travel_button,(200,500))

        #--------------------------------돈 출력--------------------------------------#
        money_Font = pg.font.Font(None,30)
        money_Text = money_Font.render("Money : " + str(money),True,black,white)
        money_Textrect = money_Text.get_rect()
        money_Textrect.center = (100,450)
        screen.blit(money_Text,money_Textrect)

  


    if (Screen == 1):
        screen.fill(black)
        #----------------------------실시간 시간 출력---------------------------------#

        date = (datetime.datetime.now()).strftime("%Y / %m / %d / %H : %M : %S")
        realtime_Font = pg.font.Font(None, 25)
        realtime_Text = realtime_Font.render("Time : " + date,True,black,white)
        realtime_Textrect = realtime_Text.get_rect()
        realtime_Textrect.center = (660,30)
        screen.blit(realtime_Text,realtime_Textrect)

        #----------------------------돈 버튼 생성 코드---------------------------------#
        money_button = pg.image.load('./Image/money_button.jpg')
        money_button = (pg.transform.scale(money_button,(100,100))).convert_alpha()
        money_b = screen.blit(money_button,(50,500))

        #---------------------------여행 버튼 생성 코드--------------------------------#
        travel_button = pg.image.load('./Image/travel_button.jpg')
        travel_button = (pg.transform.scale(travel_button,(100,100))).convert_alpha()
        travel_b = screen.blit(travel_button,(500,500))

        #--------------------------------돈 출력--------------------------------------#
        money_Font = pg.font.Font(None,30)
        money_Text = money_Font.render("Money : " + str(money),True,black,white)
        money_Textrect = money_Text.get_rect()
        money_Textrect.center = (100,450)
        screen.blit(money_Text,money_Textrect)

  
    #----------------------------이벤트 발생 코드---------------------------------#
    for event in pg.event.get():
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if money_b.collidepoint(pos):
                money += money_Add

            if travel_b.collidepoint(pos):  ### 화면 전환 이런식으로 하면 어떰
                Screen ^= 1

        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #-----------------------------화면 구현 코드----------------------------------#
    pg.display.update()
    clock.tick(FPS)