import pygame as pg

pg.init()

s = pg.display.set_mode((800,600))
s.fill((0,0,0))

f = pg.font.Font(("./Font/bmjua.ttf"), 30)#배민 주아체
t = f.render("Test, 방구석 여-행", True,(255,255,255))

s.blit(t, t.get_rect())
pg.display.update()
