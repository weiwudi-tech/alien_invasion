import pygame
import random
from pygame.sprite import Sprite


class Tools(Sprite):
    #表示单个道具
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen#访问屏幕
        self.screen_rect=ai_game.screen.get_rect()#访问屏幕作为矩形的属性，用于确定道具放置位置
        self.image=pygame.image.load("image/star.bmp")
        self.rect=self.image.get_rect()#将道具定义为矩形
        self.settings=ai_game.settings#从settings.py中取值
        #初始化外星人在屏幕左上角
        self.rect.x=random.randint(0,1130)
        self.rect.y=random.randint(500,650)
        
        self.x=float(self.rect.x)#x坐标存储为浮点数
        self.y=float(self.rect.y)#y坐标存储为浮点数

     
        

