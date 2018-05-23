import pygame
from settings import Settings
from  ship import Ship
import game_functions as gf
from pygame.sprite  import Group


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("武装飞船")
    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建子弹编组
    bullets =Group()
    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        #更新状态
        ship.update()
        gf.update_bullets(bullets)       
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
