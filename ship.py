import pygame

class Ship:
    def __init__(self,ai_game):
        #初始化飞船与设置初始位置
        self.screen=ai_game.screen#访问屏幕
        self.screen_rect=ai_game.screen.get_rect()#访问屏幕作为矩形的属性，用于确定飞船放置位置
        self.image=pygame.image.load("image/state(1).png")
        self.rect=self.image.get_rect()#将飞船视作矩形
        self.settings=ai_game.settings#从settings.py中取值
        self.rect.midbottom=self.screen_rect.midbottom#将飞船放在屏幕底部中间
        self.x=float(self.rect.x)#x坐标存储为浮点数
        self.y=float(self.rect.y)#y坐标存储为浮点数
        self.moving_right=False#飞船向右移动标志物
        self.moving_left=False#飞船向左移动标志物
        self.moving_up=False#飞船向上移动标志物
        self.moving_down=False#飞船向下移动标志物
        

    def update(self):#更新飞船位置
        if self.moving_right and self.x<self.settings.screen_width-70:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.x>0:
            self.x-=self.settings.ship_speed
        if self.moving_up and self.y>0:
            self.y-=self.settings.ship_speed
        if self.moving_down and self.y<self.settings.screen_height-70:
            self.y+=self.settings.ship_speed

        self.rect.x=self.x#我们实时获取的是self.rect.x的值，所以要对self.x重新赋值
        self.rect.y=self.y

    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom#将飞船放在屏幕底部中间
        self.x=float(self.rect.x)#x坐标存储为浮点数
        self.y=float(self.rect.y)#y坐标存储为浮点数
        self.rect.x=self.x#我们实时获取的是self.rect.x的值，所以要对self.x重新赋值
        self.rect.y=self.y

        

    def blitme(self):#绘制飞船
        self.screen.blit(self.image,self.rect)