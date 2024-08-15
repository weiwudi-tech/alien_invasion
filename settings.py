import pygame

class Settings:
    def __init__(self):
        #屏幕设置 
        self.screen_width= 1200
        self.screen_height= 720
        self.background_image=pygame.image.load("image/bg.png")
        #飞船设置
        self.ship_speed=5
        self.ship_limit=3#飞船生命
        #子弹设置
        self.bullet_speed=10
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=(0,0,0)
        #外星人设置
        self.alien_speed=1
        self.fleet_drop_speed=1
        self.fleet_direction=1#1为向右移动，-1为向左移动
