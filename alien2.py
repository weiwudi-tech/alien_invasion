import pygame
import random
from pygame.sprite import Sprite

class Alien2(Sprite):
    #表示单个外星人
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen#访问屏幕
        self.screen_rect=ai_game.screen.get_rect()#访问屏幕作为矩形的属性，用于确定外星人放置位置
        self.image=pygame.image.load("image/hanjian.png")
        self.rect=self.image.get_rect()#将外星人定义为矩形
        self.settings=ai_game.settings#从settings.py中取值
        #初始化外星人在屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)#x坐标存储为浮点数
        self.y=float(self.rect.y)#y坐标存储为浮点数
    
    def update(self):
        self.x +=self.settings.alien_speed*self.settings.fleet_direction
        self.y += self.settings.fleet_drop_speed

        self.rect.x=self.x#我们实时获取的是self.rect.x的值，所以要对self.x重新赋值
        self.rect.y=self.y

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)

     
        

