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

class Image(pg.sprite.Sprite): #rect는 sprite객체만 가능해서 만듦
    def __init__(self,fileroute,size,rect): #size랑 rect는 튜플
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(fileroute) #객체의 이미지를 설정함
        if size != -1:
            self.image = (pg.transform.scale(self.image,size)).convert_alpha()
        self.Rect = self.image.get_rect(topleft=rect)



###변경점 ----

pin_image = pg.transform.scale(pg.image.load('./Image/Pin.png'),(25,25)).convert_alpha()

national_list = ["japan", "taipei", "singapore", "russia", "austrailia", "turkey", "italy", "switzerland","south_pole", "moon", "andromeda"]
korean_name = ["이시국", "대만", "싱가포르", "러시아", "호주", "터키", "이탈리아", "스위스", "남극", "달나라", "안드로메다"]
national_pos = [(461,216),(438,249),(382,325),(319,137),(501,427),(130,192),(80,189),(45,162),(256,552),(630,160),(610,280)]
national_pos = list(map(lambda x : (x[0]+38, x[1]+12), national_pos))
national_cost = [8000,20000,40000,80000,150000,300000,800000,2000000,5000000,20000000,50000000]
national_max_money = [20000,40000,80000,150000,300000,800000,2000000,5000000,20000000,50000000]
national_select = [0 for i in range(11)]
national_clear = [0 for i in range(11)]


outer_image = [0 for i in range(2)]
national_button = [0 for i in range(11)]


Map = pg.image.load('./Image/TravelMap.png')
Map = (pg.transform.scale(Map,(800,600))).convert_alpha()

space_pos = (550,80)
Space = pg.image.load('./Image/Space1.png')
Space = (pg.transform.scale(Space,(300,400))).convert_alpha()

Moon_pos = (660,185)
Moon = pg.image.load('./Image/Moon.png')
outer_image[0] = (pg.transform.scale(Moon,(130,100))).convert_alpha()

Andromeda_pos = (650,255)
Andromeda = pg.image.load('./Image/Galaxy.png')
outer_image[1] = (pg.transform.scale(Andromeda,(150,130))).convert_alpha()

def make_travel_button(pos, cost, name, clear):
    x,y = pos
    go_travel = "여행하기" if not clear else "여행완료"
    travel_cost = "비용 : {}원".format(cost)
    go_travel_font = pg.font.Font(font, 25)
    
    gotravel_Text = go_travel_font.render(go_travel,True,black,white)
    gotravel_Textrect = gotravel_Text.get_rect()
    gotravel_Textrect.center = (x + 30, y)
    
    
    travel_cost_font = pg.font.Font(font, 25)
    travelcost_Text = travel_cost_font.render(travel_cost,True,black,white)
    travelcost_Textrect = travelcost_Text.get_rect()
    travelcost_Textrect.center = (x + 30, y - 30)
    
    name_Text = go_travel_font.render(name,True,black,white)
    name_Textrect = name_Text.get_rect()
    name_Textrect.center = (x + 30, y-60)
    
    button = screen.blit(gotravel_Text, gotravel_Textrect)
    screen.blit(travelcost_Text, travelcost_Textrect)
    screen.blit(name_Text, name_Textrect)

    return button

def travel(currentscene):
    lst = []
    national_name = national_list[currentscene-20]

    if currentscene != 20:
        lst.append(Image('./Image/Travel_Images/travel1.png',(600,300),(215,100)))
        lst.append(Image('./Image/Travel_Images/travel2.png',(600,300),(415,100)))

    for i in range(2):
        lst.append(Image('./Image/Travel_Images/{}{}.png'.format(national_name, i+1),(600,300),(0,100)))
    return lst


def processing_bar(currentscene):
    
    lt = (100,480)
    wh = (600,25)
    percent = 0

    background = Image("./Image/background.jpg",-1,(0,0))

    toggle = 0

    image_list = travel(currentscene)
    while percent<100:
        screen.blit(background.image, background.Rect)
        screen.blit(image_list[toggle].image, image_list[toggle].Rect)
        if currentscene != 20:
            screen.blit(image_list[toggle+2].image, image_list[toggle+2].Rect)
        
        if 0 <= percent%20 <= 0.1:
            toggle ^= 1
            
        percent = percent%100+0.5
        
        r = pg.Rect((100,530), (wh[0]/100*percent, 25))
        pg.draw.rect(screen,(0,0,0),r)
        
        pg.display.update()
        pg.time.wait(20)
    pg.event.clear()

###------------

travel_button = None

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

    Map_blit = screen.blit(Map,(-75,0))
    Space_blit = screen.blit(Space,space_pos)
    national_button[9] = screen.blit(outer_image[0],national_pos[9])
    national_button[10] = screen.blit(outer_image[1],national_pos[10])

    for i in range(9):
        national_button[i] = screen.blit(pin_image,national_pos[i])

    
    for i in range(11):
        if national_select[i]:
            travel_button = make_travel_button(national_pos[i], national_cost[i], korean_name[i], national_clear[i])

  


    #----------------------------이벤트 발생 코드---------------------------------#
    for event in pg.event.get():
        
      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        pos = pg.mouse.get_pos()

        if travel_button != None and travel_button.collidepoint(pos) and not national_clear[national_count]:
            national_cost[national_count]#필요한 비용
            ##비용확인 후 시도하기
            national_clear[national_count] = 1
            processing_bar(national_count+20)
            player.maxmoney = national_max_money[national_count]

        for i in range(11):
            if national_button[i].collidepoint(pos):
                national_select = [0 for i in range(11)]
                national_select[i] = 1
                national_count = i

        
                


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
