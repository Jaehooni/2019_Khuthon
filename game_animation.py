import pygame as pg
import random


pg.init()
screen_width = 800
screen_height = 600
size = [screen_width, screen_height]
FPS = 60
white = (255,255,255)
black = (0,0,0)
screen = pg.display.set_mode(size) # 창크기 설정
pg.display.set_caption("가제 : 방구석 여ㅡ행")

#필요한 변수들 선언
cup_image = pg.image.load("./Image/yabawi.png")

bmjuaFont = pg.font.Font("./Font/bmjua.ttf", 30)
posX = 315
distance = 250

reward = random.randint(2,11)
reward_text = bmjuaFont.render(str(reward)+"배", True, black)

reward_pos = random.randint(-1,1)


#보여주는 모션
def open_cup(pos):
    reward_rect = reward_text.get_rect()
    reward_rect.center = (posX+reward_pos*distance+85, 370)
    i = -5
    while i < 300:
        i+=1
        if 100 < i < 200 :
            continue;
        
        screen.fill(white)
        screen.blit(reward_text, reward_rect)
        
        dh = 150 - abs(150-i)

        screen.blit(cup_image, (posX-distance, 200-(pos==-1)*dh))
        screen.blit(cup_image, (posX, 200-(pos==0)*dh))
        screen.blit(cup_image, (posX+distance, 200-(pos==1)*dh))

        pg.display.update()
        pg.time.wait(1)

open_cup(reward_pos)

pg.time.wait(100)

#섞는 모션
cup = list(range(3))
for i in range(3):
    distance = 250
    while distance > -255:
        screen.fill(white)

        dw = 50-abs(distance)/5
        dh = int(200-dw/2)
        
        con_cup_image = pg.transform.scale(cup_image,(int(171+0.85*dw), int(207+dw))).convert_alpha()

        screen.blit(con_cup_image, (posX-distance, dh))
        screen.blit(con_cup_image, (posX, dh))
        screen.blit(con_cup_image, (posX+distance, dh))

        pg.display.update()

        distance-=5
        pg.time.wait(1)

distance = 250
cup[0] = screen.blit(cup_image, (posX-distance, 200))
cup[1] = screen.blit(cup_image, (posX, 200))
cup[2] = screen.blit(cup_image, (posX+distance, 200))

#이벤트 코드
pg.event.clear()
clicked = False
clicked_pos = 0
reward_pos = random.randint(-1,1)

while not clicked:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()

            for i in range(3):
                if cup[i].collidepoint(pos):
                    clicked = True
                    clicked_pos = i-1

#결과 모션
open_cup(clicked_pos)
pg.time.wait(100)

if clicked_pos != reward_pos:
    open_cup(reward_pos)

else:
    re_motion = [pg.image.load("./Image/reward1.png"), pg.image.load("./Image/reward2.png")]
    re_motion_pos = [(130,20),(125,60)]

    for i in range(6):
        screen.fill(white)
        screen.blit(re_motion[i%2], re_motion_pos[i%2])
        screen.blit(reward_text, (379,285))
        pg.display.update()
        pg.time.wait(500)
