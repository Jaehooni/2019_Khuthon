import pygame as pg
import random
import pygame_textinput as text


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
ui_image = pg.image.load("./Image/a_ui.png")

bmjuaFont = pg.font.Font("./Font/bmjua.ttf", 30)
posX = 315
posY = 180
distance = 250

reward = random.randint(2,11)
reward_text = bmjuaFont.render(str(reward)+"배", True, black)

reward_pos = random.randint(-1,1)

#UI 유지용
def make_ui():
    screen.blit(ui_image, (0,444))


#보여주는 모션
def open_cup(pos):
    reward_rect = reward_text.get_rect()
    reward_rect.center = (posX+reward_pos*distance+85, posY+170)
    i = -5
    while i < 300:
        i+=1
        if 100 < i < 200 :
            continue;
        
        screen.fill(white)

        make_ui()
        
        screen.blit(reward_text, reward_rect)
        
        dh = 150 - abs(150-i)

        screen.blit(cup_image, (posX-distance, posY-(pos==-1)*dh))
        screen.blit(cup_image, (posX, posY-(pos==0)*dh))
        screen.blit(cup_image, (posX+distance, posY-(pos==1)*dh))

        pg.display.update()
        pg.time.wait(1)


def shake_and_result():
    global reward_pos
    open_cup(reward_pos)

    pg.time.wait(100)

    #섞는 모션
    cup = list(range(3))
    for i in range(3):
        distance = 250
        while distance > -255:
            screen.fill(white)

            make_ui()

            dw = 50-abs(distance)/5
            dh = int(posY-dw/2)
            
            con_cup_image = pg.transform.scale(cup_image,(int(171+0.85*dw), int(207+dw))).convert_alpha()

            screen.blit(con_cup_image, (posX-distance, dh))
            screen.blit(con_cup_image, (posX, dh))
            screen.blit(con_cup_image, (posX+distance, dh))

            pg.display.update()

            distance-=5
            pg.time.wait(1)

    distance = 250
    cup[0] = screen.blit(cup_image, (posX-distance, posY))
    cup[1] = screen.blit(cup_image, (posX, posY))
    cup[2] = screen.blit(cup_image, (posX+distance, posY))

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
        for i in range(2):
            re_motion[i] = pg.transform.scale(re_motion[i], (400,400))
        re_motion_pos = [(210,15),(210,30)]

        for i in range(6):
            screen.fill(white)

            make_ui()
            
            screen.blit(re_motion[i%2], re_motion_pos[i%2])
            screen.blit(reward_text, (379,207))
            pg.display.update()
            pg.time.wait(500)

textinput = text.TextInput(initial_string="                         ")
textinput.text_color = (255,255,255)
end = False
while not end:
    events = pg.event.get()

    get_text = textinput.get_text()
        
    if textinput.update(events) and get_text:
        end = True    
          
    screen.blit(textinput.get_surface(), (30,80))

    pg.display.update()
    pg.time.wait(30)

shake_and_result()


