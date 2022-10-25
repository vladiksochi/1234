import pygame as pg
import sys
import controls
from gun import Gun
from pygame.sprite import Group

def run():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Вселенская битва")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)



run()