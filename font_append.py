import pygame as pg

pg.init()

s = pg.display.set_mode((800,600))

while True:
    s.fill((0,0,0))
    f = pg.font.Font(("./Font/bmjua.ttf"), 45)#배민 주아체
    t = f.render("최대보유자금이 ~ 증가했습니다", True,(255,255,255))
    s.blit(t, t.get_rect())
    pg.display.update()
