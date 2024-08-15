import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):#管理所有发射的子弹
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen#访问屏幕
        #从settings.py中取值
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)#在（0，0）处创建子弹
        self.rect.midtop=ai_game.ship.rect.midtop#将子弹移到飞船正上方
        self.x=float(self.rect.x)#x坐标存储为浮点数
        self.y=float(self.rect.y)#y坐标存储为浮点数

    def update(self):#更新子弹位置
        self.y-=self.settings.bullet_speed

        self.rect.y=self.y#我们实时获取的是self.rect.y的值，所以要对self.y重新赋值

    def draw_bullet(self):#自己绘制的矩形非外来图片，不用blit函数
        pygame.draw.rect(self.screen,self.color,self.rect)

