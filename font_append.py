import pygame as pg
import os

pg.init()

s = pg.display.set_mode((800,600))
s.fill((0,0,0))

f = pg.font.Font(os.path.abspath("Font/bmjua.ttf"), 30)#배민 주아체, 절대경로를 써야 오류가 안 뜸
t = f.render("Test, 방구석 여-행", True,(255,255,255))

s.blit(t, t.get_rect())
pg.display.update()
