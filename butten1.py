import pygame.font

class Button1:
    def __init__(self,ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        #设置按钮尺寸
        self.width,self.height=200,50
        self.button_color=(255,0,0)
        self.text_color=(255,255,0)
        self.font=pygame.font.SysFont(None,48)#设置字体
        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #按钮显示的文字
        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #绘制按钮与文字
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        