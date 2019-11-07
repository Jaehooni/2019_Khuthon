import pygame as pg
import sys
import time
import random
import datetime
'''
pg.init()
FPS = 60
screen_width = 800
screen_height = 600
white = (255,255,255)
black = (0,0,0)
screen = pg.display.set_mode((screen_width,screen_height)) #창 크기 설정
pg.display.set_caption('PYSOUL')
clock = pg.time.Clock()

while True:
    for event in pg.event.get(): #파이게임 종료
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    clock.tick(FPS)
'''
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


currentscene = 0 #현재 secne 번호
class Image(pg.sprite.Sprite): #rect는 sprite객체만 가능해서 만듦
    def __init__(self,fileroute,size,rect): #size랑 rect는 튜플
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(fileroute) #객체의 이미지를 설정함
        self.image = (pg.transform.scale(self.image,size)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = rect

image0 = Image('./Image/button.jpg',(200,100),(0,0)) #image0이라는 sprite객체가 만들어짐
image1 = Image('./Image/button.jpg',(200,200),(0,0)) #image0을 screenblit하면 안됨(image0은 이미지가아님)
image2 = Image('./Image/button.jpg',(200,300),(0,0)) #image0.image가 출력가능한것

scenelist = [[],[],[]] #내부의리스트는 하나의 게임씬(0번 씬,1번 씬...)
scenelist[0].append(image0) #먼저 image0을 0번씬에 출력함
scenelist[1].append(image1)
scenelist[2].append(image2)

def scene_change_blit(currentscene): #특수한 경우가 아니면 출력은 이걸로 하는게 좋을듯
    for sprite in scenelist[currentscene]: #현재 scene에 해당하는 이미지들을 담은 리스트 요소들을 출력
        screen.blit(sprite.image,sprite.rect)

#기존 버튼 크기만 다르게 해놔서 씬 넘어가는 느낌만 나게 해봄
#실전에선 각기 다른이미지들을 쓰면 됨

while True:
    screen.fill(white)
    #----------------------------실시간 시간 출력---------------------------------#

    date = (datetime.datetime.now()).strftime("%Y / %m / %d / %H : %M : %S")
    realtime_Font = pg.font.Font(None, 25)
    realtime_Text = realtime_Font.render("Time : " + date,True,black,white)
    realtime_Textrect = realtime_Text.get_rect()
    realtime_Textrect.center = (660,30)
    screen.blit(realtime_Text,realtime_Textrect)

    scene_change_blit(currentscene)

    for event in pg.event.get():
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if pos[0] > 0 and pos[1] > 0: #대충 화면클릭하면 currenntscene을 증가시킴
                currentscene += 1
                if currentscene >2:
                    currentscene = 0


        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    clock.tick(FPS)