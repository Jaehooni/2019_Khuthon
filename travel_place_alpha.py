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
        self.maxmoney = 200000
        self.happiness = 0
        self.stamina = 100
        self.day = 1

player = Player()


currentscene = 10 #현재 secne 번호
class Image(pg.sprite.Sprite): #rect는 sprite객체만 가능해서 만듦
    def __init__(self,fileroute,size,rect): #size랑 rect는 튜플
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(fileroute) #객체의 이미지를 설정함
        if size != -1:
            self.image = (pg.transform.scale(self.image,size)).convert_alpha()
        self.Rect = self.image.get_rect(topleft=rect)

intro_background = Image('./Image/Intro_background.png',(850,650),(-30,-15))
#---0---
main_background = Image('./Image/main_background.png',-1,(0,0))
go_alba = Image('./Image/go_alba.png',-1,(18,68))
go_stat = Image('./Image/go_stat.png',-1,(18,180))
go_travel = Image('./Image/go_travel.png',-1,(18,292))
#---1---
ui = Image('./Image/a_ui2.png',-1,(0,444)) 
stamina_gauge = Image('./Image/stamina_gauge.png',-1,(625,541)) #width=158 height=25

alba1_1 = Image('./Image/alba1_1.png',-1,(95,50)) 
alba1_2 = Image('./Image/alba1_2.png',-1,(95,175)) 
alba1_3 = Image('./Image/alba1_3.png',-1,(95,300))
backmove = Image('./Image/backmove.png',-1,(3,168))
frontmove = Image('./Image/frontmove.png',-1,(747,168))
#---2---
alba2_1 = Image('./Image/alba2_1.png',-1,(95,50)) 
alba2_2 = Image('./Image/alba2_2.png',-1,(95,175)) 
alba2_3 = Image('./Image/alba2_3.png',-1,(95,300))
#---3---
alba3_1 = Image('./Image/alba3_1.png',-1,(95,50)) 
alba3_2 = Image('./Image/alba3_2.png',-1,(95,175)) 
alba3_3 = Image('./Image/alba3_3.png',-1,(95,300))
#---4---
int1 = Image('./Image/int1.png',-1,(95,50))
int2 = Image('./Image/int2.png',-1,(95,175)) 
int3 = Image('./Image/int3.png',-1,(95,300))
#---5---
heal1 = Image('./Image/heal1.png',-1,(95,50))
heal2 = Image('./Image/heal2.png',-1,(95,175)) 
heal3 = Image('./Image/heal3.png',-1,(95,300))

#---6---
charm1 = Image('./Image/charm1.png',-1,(95,50))
charm2 = Image('./Image/charm2.png',-1,(95,175)) 
charm3 = Image('./Image/charm3.png',-1,(95,300))

#나라(1) = 그냥 여행지 사진, 나라(2) = 여행 진행중 사진 추후 첨부
#나라(3) -> 1번과 동일하나 여행하기 버튼이 여행완료로 바뀐 형태

#---20---이시국 여행지 사진 첨부
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---21---대만
Goback = Image('./Image/Before.jpg',(200,100),(15,480))

Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---22---싱가폴
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---23---러시아
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---24---호주
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---25---터키
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---26---이탈리아
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---27---스위스
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---28---남극
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---29---달
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#------안드로메다
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))


#---30---이시국(2)
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
#---31---대만(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---32---싱가폴(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---33---러시아(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---34---호주(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---35---터키(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---36---이탈리아(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---37---스위스(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---38---남극(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#---39---달(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))
#------안드로메다(2)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel = Image('./Image/Travel.png',(200,100),(293,480))


#---40---이시국(3)
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---41---대만(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---42---싱가폴(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---43---러시아(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---44---호주(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---45---터키(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---46---이탈리아(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---47---스위스(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---48---남극(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---49---달(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#------안드로메다(3)
Goback = Image('./Image/Before.jpg',(200,100),(15,480))
Gonext = Image('./Image/Next.jpg',(200,100),(600,480))
Travel_complete = Image('./Image/travel_complete.png',(200,100),(293,480))
#---53---능력치 상승
f = pg.font.Font(("./Font/bmjua.ttf"), 30)#배민 주아체
t = f.render("Test, 방구석 여-행", True,(255,255,255))
#s.blit(t, t.get_rect())
scenelist = []
for i in range(0, 60):
    scenelist.append([])
scenelist[0].extend([main_background,go_alba,go_stat,go_travel])
scenelist[1].extend([alba1_1,alba1_2,alba1_3,backmove,frontmove])
scenelist[2].extend([alba2_1,alba2_2,alba2_3,backmove,frontmove])
scenelist[4].extend([int1,int2,int3,backmove,frontmove])
scenelist[5].extend([heal1,heal2,heal3,backmove,frontmove])
scenelist[6].extend([charm1,charm2,charm3,backmove])
scenelist[10].extend([intro_background]) #인트로
scenelist[20].extend([Gonext, Travel])
scenelist[21].extend([Gonext, Goback, Travel])
scenelist[22].extend([Gonext, Goback, Travel])
scenelist[23].extend([Gonext, Goback, Travel])
scenelist[24].extend([Gonext, Goback, Travel])
scenelist[25].extend([Gonext, Goback, Travel])
scenelist[26].extend([Gonext, Goback, Travel])
scenelist[27].extend([Gonext, Goback, Travel])
scenelist[28].extend([Gonext, Goback, Travel])
scenelist[29].extend([Gonext, Goback, Travel])
scenelist[30].extend([Gonext, Travel])
scenelist[31].extend([Gonext, Goback, Travel])
scenelist[32].extend([Gonext, Goback, Travel])
scenelist[33].extend([Gonext, Goback, Travel])
scenelist[34].extend([Gonext, Goback, Travel])
scenelist[35].extend([Gonext, Goback, Travel])
scenelist[36].extend([Gonext, Goback, Travel])
scenelist[37].extend([Gonext, Goback, Travel])
scenelist[38].extend([Gonext, Goback, Travel])
scenelist[39].extend([Gonext, Goback, Travel])
scenelist[40].extend([Gonext, Travel])
scenelist[41].extend([Gonext, Goback, Travel])
scenelist[42].extend([Gonext, Goback, Travel])
scenelist[43].extend([Gonext, Goback, Travel])
scenelist[44].extend([Gonext, Goback, Travel])
scenelist[45].extend([Gonext, Goback, Travel])
scenelist[46].extend([Gonext, Goback, Travel])
scenelist[47].extend([Gonext, Goback, Travel])
scenelist[48].extend([Gonext, Goback, Travel])
scenelist[49].extend([Gonext, Goback, Travel])
scenelist[50].extend([Gonext, Travel])
scenelist[51].extend([Gonext, Goback, Travel])
scenelist[52].extend([Gonext, Goback, Travel])
scenelist[53].extend([Gonext, Goback, Travel])

def fade_in_and_out():
    fade = 255
    fade_image = pg.Surface((800,600), pg.SRCALPHA)
    pg.draw.rect(fade_image, (0,0,0,10), fade_image.get_rect())
    ui_blit()   
    while fade > 0: 
        screen.blit(fade_image,fade_image.get_rect())
        fade -=1
        pg.display.update()
        pg.time.wait(1) 

def scene_change_blit(currentscene): 
    for sprite in scenelist[currentscene]:
        screen.blit(sprite.image,sprite.Rect)

def ui_blit(): #ui출력용,currentscene받아서 특정씬에는 안돌리게 하면됨
    screen.blit(ui.image,ui.Rect)
    screen.blit(stamina_gauge.image,stamina_gauge.Rect)

    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render(str(player.money),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(343,506)
    screen.blit(text,textrect)

    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render(str(player.day),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(343,545)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.health),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,470)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.intelligence),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,518)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.charm),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(127,561)
    screen.blit(text,textrect)

    text = realtime_Font.render(str(player.maxmoney),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(626,479)
    screen.blit(text,textrect)

def alba_lock(stat,min_stat):
    if stat >= min_stat:
        return True
    return False

def stamina_update(player,stamina_gauge): #스태미나 게이지 조절용
    if player.stamina <= 0:
        player.stamina = 0
    stamina_gauge.image = pg.transform.scale(stamina_gauge.image,(int(158*player.stamina/100),25))

def day_pass():
    global currentscene
    if player.stamina ==0:
        currentscene = 0
        player.day += 1
        player.stamina = 100
        fade_in_and_out()
        pg.event.clear()
        

def money_decline(player,decline): #돈없으면 업글못해
    if player.money < decline:
        return False
    else:
        player.money -= decline
        player.stamina -= 10
        return True

while True:
    screen.fill(white)

    stamina_update(player,stamina_gauge)

    scene_change_blit(currentscene)

    ui_blit()

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if currentscene == 10:
                if intro_background.Rect.collidepoint(pos):
                    currentscene = 0
            elif currentscene == 0:
                if go_alba.Rect.collidepoint(pos):
                    currentscene = 1
                elif go_stat.Rect.collidepoint(pos):
                    currentscene = 4
            elif currentscene == 1:
                if alba1_1.Rect.collidepoint(pos):
                    player.money += 5000 
                    player.stamina -= 10
                    lt = (100,480)
                    wh = (600,25)
                    percent = 0
                    while percent<100:
                        screen.fill((0,0,0))
                        percent = percent%100+0.5
                        r = pg.Rect((100,530), (wh[0]/100*percent, 25))
                        pg.draw.rect(screen,(255,255,255),r)

    
                        pg.display.update()
                        pg.time.delay(1)
                elif alba1_2.Rect.collidepoint(pos):
                    player.money += 100000 * alba_lock(player.intelligence,10)
                    player.stamina -= 10 * alba_lock(player.intelligence,10)
                elif alba1_3.Rect.collidepoint(pos):
                    player.money += 2000000 * alba_lock(player.intelligence,50)
                    player.stamina -= 10 * alba_lock(player.intelligence,50)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 2
            elif currentscene == 2:
                if alba2_1.Rect.collidepoint(pos):
                    player.money += 10000
                    player.stamina -= 10
                elif alba2_2.Rect.collidepoint(pos):
                    player.money += 200000 * alba_lock(player.health,10)
                    player.stamina -= 10 * alba_lock(player.health,10)
                elif alba2_3.Rect.collidepoint(pos):
                    player.money += 10000000 * alba_lock(player.health,100)
                    player.stamina -= 10 * alba_lock(player.health,100)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 1
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 3
            elif currentscene == 3:
                if alba3_1.Rect.collidepoint(pos):
                    player.money += 5000
                    player.stamina -= 10
                elif alba3_2.Rect.collidepoint(pos):
                    player.money += 100000 * alba_lock(player.charm,10)
                    player.stamina -= 10 * alba_lock(player.charm,10)
                elif alba3_3.Rect.collidepoint(pos):
                    player.money += 2000000 * alba_lock(player.charm,50)
                    player.stamina -= 10 * alba_lock(player.charm,50)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 2
            elif currentscene == 4:
                if int1.Rect.collidepoint(pos):
                    player.intelligence += 1 * money_decline(player,30000)
                elif int2.Rect.collidepoint(pos):
                    player.intelligence += 5 * money_decline(player,1000000)
                elif int3.Rect.collidepoint(pos):
                    player.intelligence += 50 * money_decline(player,10000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 0   
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 5 
            elif currentscene == 5:
                if heal1.Rect.collidepoint(pos):
                    player.health += 1 * money_decline(player,50000)
                elif heal2.Rect.collidepoint(pos):
                    player.health += 5 * money_decline(player,2500000)
                elif heal3.Rect.collidepoint(pos):
                    player.health += 10 * money_decline(player,50000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 4   
                elif frontmove.Rect.collidepoint(pos):
                    currentscene = 6 
            elif currentscene == 6:
                if int1.Rect.collidepoint(pos):
                    player.charm += 1 * money_decline(player,30000)
                elif int2.Rect.collidepoint(pos):
                    player.charm += 5 * money_decline(player,1000000)
                elif int3.Rect.collidepoint(pos):
                    player.charm += 50 * money_decline(player,10000000)
                elif backmove.Rect.collidepoint(pos):
                    currentscene = 5  

        if event.type == pg.QUIT:
            pg.quit()
            quit()
 
    #test용
    realtime_Font = pg.font.Font(None, 25)
    text = realtime_Font.render('cursor = '+str(pg.mouse.get_pos()),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(0,0)
    screen.blit(text,textrect)

    text = realtime_Font.render('scene = '+str(currentscene),True,(0,0,0))
    textrect = text.get_rect()
    textrect.topleft =(700,0)
    screen.blit(text,textrect)


    pg.display.update()
    clock.tick(FPS)