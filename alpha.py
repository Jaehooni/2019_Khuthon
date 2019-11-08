import pygame as pg
import sys
import time
import random
import datetime
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

class Player():
    def __init__(self):
        self.health = 1
        self.intelligence = 1
        self.charm = 1
        self.money = 10
        self.happiness = 0
player = Player()


currentscene = 0 #현재 secne 번호
class Image(pg.sprite.Sprite): #rect는 sprite객체만 가능해서 만듦
    def __init__(self,fileroute,size,rect): #size랑 rect는 튜플
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(fileroute) #객체의 이미지를 설정함
        if size != -1:
            self.image = (pg.transform.scale(self.image,size)).convert_alpha()
        self.Rect = self.image.get_rect(topleft=rect)

#---0---
main_background = Image('./Image/main_background.png',-1,(0,0))
go_alba = Image('./Image/go_alba.png',-1,(18,68))
go_stat = Image('./Image/go_stat.png',-1,(18,180))

#---1---
ui = Image('./Image/a_ui.png',-1,(0,444)) 
alba1_1 = Image('./Image/alba1_1.png',-1,(95,50)) 
alba1_2 = Image('./Image/alba1_2.png',-1,(95,175)) 
alba1_3 = Image('./Image/alba1_3.png',-1,(95,300))
backmove = Image('./Image/backmove.png',-1,(3,168))
frontmove = Image('./Image/frontmove.png',-1,(747,168))
#---2---
alba2_1 = Image('./Image/alba2_1.png',-1,(95,50)) 
alba2_2 = Image('./Image/alba2_2.png',-1,(95,175)) 
alba2_3 = Image('./Image/alba2_3.png',-1,(95,300))
#---4---
int1 = Image('./Image/int1.png',-1,(95,50))
int2 = Image('./Image/int2.png',-1,(95,175)) 
int3 = Image('./Image/int3.png',-1,(95,300))
#---5---
heal1 = Image('./Image/heal1.png',-1,(95,50))
heal2 = Image('./Image/heal2.png',-1,(95,175)) 
heal3 = Image('./Image/heal3.png',-1,(95,300))

scenelist = [[],[],[],[],[],[],[],[],[]] 
scenelist[0].extend([main_background,ui,go_alba,go_stat])
scenelist[1].extend([ui,alba1_1,alba1_2,alba1_3,backmove,frontmove])
scenelist[2].extend([ui,alba2_1,alba2_2,alba2_3,backmove,frontmove])
scenelist[4].extend([ui,int1,int2,int3,backmove,frontmove])
scenelist[5].extend([ui,heal1,heal2,heal3,backmove,frontmove])

def scene_change_blit(currentscene): 
    for sprite in scenelist[currentscene]:
        screen.blit(sprite.image,sprite.Rect)

while True:
    screen.fill(white)

    realtime_Font = pg.font.Font(None, 25)
    scene_change_blit(currentscene)

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if currentscene == 0:
                if go_alba.Rect.collidepoint(pos):
                    currentscene = 1
                elif go_stat.Rect.collidepoint(pos):
                    currentscene = 4
            elif currentscene == 1:
                if alba1_1.Rect.collidepoint(pos):
                    player.money += 5000
                elif alba1_2.Rect.collidepoint(pos):
                    player.money += 100000
                elif alba1_3.Rect.collidepoint(pos):
                    player.money += 2000000
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 2
            elif currentscene == 2:
                if alba2_1.Rect.collidepoint(pos):
                    player.money += 10000
                elif alba2_2.Rect.collidepoint(pos):
                    player.money += 200000
                elif alba2_3.Rect.collidepoint(pos):
                    player.money += 10000000
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 1
            elif currentscene == 4:
                if int1.Rect.collidepoint(pos):
                    player.money -= 30000
                    player.intelligence += 1
                elif int2.Rect.collidepoint(pos):
                    player.money -= 1000000
                    player.intelligence += 5
                elif int3.Rect.collidepoint(pos):
                    player.money -= 10000000
                    player.intelligence += 10
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0   
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 5 
            elif currentscene == 5:
                if int1.Rect.collidepoint(pos):
                    player.money -= 50000
                    player.health += 1
                elif int2.Rect.collidepoint(pos):
                    player.money -= 2500000
                    player.health += 5
                elif int3.Rect.collidepoint(pos):
                    player.money -= 50000000
                    player.health += 10
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 4    
        if event.type == pg.QUIT:
            pg.quit()
            quit()
 
    text = realtime_Font.render('cursor = '+str(pg.mouse.get_pos()),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(0,0)
    screen.blit(text,textrect)

    text = realtime_Font.render('scene = '+str(currentscene),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(700,0)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.money),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(343,506)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.health),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,470)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.intelligence),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,518)
    screen.blit(text,textrect)

    pg.display.update()
    clock.tick(FPS)