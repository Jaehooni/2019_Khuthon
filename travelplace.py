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
font = "./Font/bmjua.ttf"


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

    national_list = ["japan", "taipei", "singapore", "russia", "austrailia", "turkey", "italy", "switzerland","south_pole", "andromeda", "andromeda"]


    Map = pg.image.load('./Image/TravelMap.png')
    Map = (pg.transform.scale(Map,(800,600))).convert_alpha()
    Map_blit = screen.blit(Map,(-75,0))

    space_pos = (550,80)
    space_x = 550
    space_y = 80
    Space = pg.image.load('./Image/Space1.png')
    Space = (pg.transform.scale(Space,(300,400))).convert_alpha()
    Space_blit = screen.blit(Space,space_pos)

    Moon_pos = (660,185)
    Moon_x = 660
    Moon_y = 185
    Moon = pg.image.load('./Image/Moon.png')
    Moon = (pg.transform.scale(Moon,(130,100))).convert_alpha()
    Moon_blit = screen.blit(Moon,Moon_pos)

    Andromeda_pos = (650,255)
    Andromeda_x = 650
    Andromeda_y = 255
    Andromeda = pg.image.load('./Image/Galaxy.png')
    Andromeda = (pg.transform.scale(Andromeda,(170,185))).convert_alpha()
    Andromeda_blit = screen.blit(Andromeda,Andromeda_pos)

    Japan_pos = (461,216)
    Japan_x = 461
    Japan_y = 216
    Japan = pg.image.load('./Image/Pin.png')
    Japan = (pg.transform.scale((Japan),(100,50))).convert_alpha()
    Japan_blit = screen.blit(Japan,Japan_pos)

    Taiwan_pos = (438,249)
    Taiwan_x = 438
    Taiwan_y = 249
    Taiwan = pg.image.load('./Image/Pin.png')
    Taiwan = (pg.transform.scale((Taiwan),(100,50))).convert_alpha()
    Taiwan_blit= screen.blit(Taiwan,Taiwan_pos)

    Singapore_pos = (382,325)
    Singapore_x = 382
    Singapore_y = 325
    Singapore = pg.image.load('./Image/Pin.png')
    Singapore = (pg.transform.scale((Singapore),(100,50))).convert_alpha()
    Singapore_blit = screen.blit(Singapore,Singapore_pos)

    Russia_pos = (319,137)
    Russia_x = 319
    Russia_y = 137
    Russia = pg.image.load('./Image/Pin.png')
    Russia = (pg.transform.scale((Russia),(100,50))).convert_alpha()
    Russia_blit = screen.blit(Russia,Russia_pos)

    Austrailia_pos = (501,427)
    Austarailia_x = 501
    Austrailia_y = 427
    Austrailia = pg.image.load('./Image/Pin.png')
    Austrailia = (pg.transform.scale(Austrailia,(100,50))).convert_alpha()
    Austrailia_blit = screen.blit(Austrailia,Austrailia_pos)

    Turkey_pos = (130,192)
    Turkey_x = 130
    Turkey_y = 192
    Turkey = pg.image.load('./Image/Pin.png')
    Turkey = (pg.transform.scale(Turkey,(100,50))).convert_alpha()
    Turkey_blit = screen.blit(Turkey,Turkey_pos)

    Italy_pos = (80,189)
    Italy_x = 80
    Italy_y = 189
    Italy = pg.image.load('./Image/Pin.png')
    Italy = (pg.transform.scale(Italy,(100,50))).convert_alpha()
    Italy_blit = screen.blit(Italy,Italy_pos)

    Switzerland_pos = (45,162)
    Switzerland_x = 45
    Switzerland_y = 162
    Switzerland = pg.image.load('./Image/Pin.png')
    Switzerland = (pg.transform.scale(Italy,(100,50))).convert_alpha()
    Switzerland_blit = screen.blit(Switzerland,Switzerland_pos)

    South_pole_pos = (256,552)
    South_pole_x = 256
    South_pole_y = 552
    South_Pole = pg.image.load('./Image/Pin.png')
    South_Pole = (pg.transform.scale(South_Pole,(100,50))).convert_alpha()
    South_Pole_blit = screen.blit(South_Pole,South_pole_pos)

    def make_travel_button(x, y, cost = 0):
      go_travel = "여행하기"
      travel_cost = "비용 : {}원".format(cost)
      go_travel_font = pg.font.Font(font, 25)
      gotravel_Text = go_travel_font.render(go_travel,True,black,white)
      gotravel_Textrect = gotravel_Text.get_rect()
      gotravel_Textrect.center = (x + 30,216)
      screen.blit(gotravel_Text, gotravel_Textrect)
      travel_cost_font = pg.font.Font(font, 25)
      travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
      travelcost_Textrect = travelcost_Text.get_rect()
      travelcost_Textrect.center = (x + 30, y - 30)
      screen.blit(travelcost_Text, travelcost_Textrect)
    

  


    #----------------------------이벤트 발생 코드---------------------------------#
    for event in pg.event.get():
        
      ##  if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
       ##     pos = pg.mouse.get_pos()
       ##     if b.collidepoint(pos):
       ##         money += money_Add
      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        pos = pg.mouse.get_pos()
        if Japan_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Taiwan_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Singapore_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Russia_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Austrailia_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Turkey_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Italy_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if Switzerland_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)

        if South_Pole_blit.collidepoint(pos):
          go_travel = "여행하기"
          travel_cost = "비용 : 5000원"
          go_travel_font = pg.font.Font(font, 25)
          gotravel_Text = go_travel_font.render(go_travel,True,black,white)
          gotravel_Textrect = gotravel_Text.get_rect()
          gotravel_Textrect.center = (Japan_x + 30,216)
          screen.blit(gotravel_Text, gotravel_Textrect)
          travel_cost_font = pg.font.Font(font, 25)
          travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
          travelcost_Textrect = travelcost_Text.get_rect()
          travelcost_Textrect.center = (Japan_x + 30, Japan_y - 30)
          screen.blit(travelcost_Text, travelcost_Textrect)
      

        """
        #이전으로 버튼
        Goback = pg.image.load('./Image/Before.jpg')
        Goback = (pg.transform.scale(Goback,(200,100))).convert_alpha()
        back = screen.blit(Goback,(15,480))

        #다음으로 버튼
        Gonext = pg.image.load('./Image/Next.jpg')
        Gonext = (pg.transform.scale(Gonext,(200,100))).convert_alpha()
        next = screen.blit(Gonext,(600,480))

        #여행하기 버튼  
        Travel = pg.image.load('./Image/Travel.png')
        Travel =  (pg.transform.scale(Travel,(200,100))).convert_alpha()
        Travelbutton = screen.blit(Travel, (293,480))

        #여행완료 버튼
        Travel_complete = pg.image.load('./Image/travel_complete.png')
        Travel_complete =  (pg.transform.scale(Travel,(200,100))).convert_alpha()
        Travel_complete_button = screen.blit(Travel, (293,480))
        #Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
        #여행하기 버튼을 눌럿을때 프로세싱 바
        lt = (100,480)
        wh = (600,25)

        percent = 0
        while percent<100:
          screen.fill((0,0,0))
          percent = percent%100+0.5
          r = pg.Rect((100,530), (wh[0]/100*percent, 25))
          pg.draw.rect(screen,(255,255,255),r)

  
          pg.display.update()
          pg.time.delay(20)
          if percent == 100:
            break
      """
           

      if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    clock.tick(FPS)