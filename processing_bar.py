import pygame as pg


s = pg.display.set_mode((800,600))
clock = pg.time.Clock()

lt = (100,480)
wh = (600,40)

percent = 0
while percent<100:
    s.fill((0,0,0))
    percent = percent%100+0.5
    r = pg.Rect((100,480), (wh[0]/100*percent, 40))
    pg.draw.rect(s,(255,255,255),r)

    
    pg.display.update()
    pg.time.delay(10)

    
