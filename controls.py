import pygame as pg, sys
from bullet import Bullet

def events(screen, gun, bullets): #Обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT: #Кнопка вправо
                gun.mright = True
            elif event.key == pg.K_LEFT: #Кнопка влево
                gun.mleft = True
            elif event.key == pg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pg.KEYUP: #Кнопка вправо
            if event.key == pg.K_RIGHT:
                gun.mright = False
            elif event.key == pg.K_LEFT: #Кнопка влево
                gun.mleft = False

def update(bg_color, screen, gun, bullets): #Обновление экрана
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pg.display.flip()

