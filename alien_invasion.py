#调用区域
import sys
import time 
import pygame
import os
import random
from settings import Settings 
from ship import Ship
from bullets import Bullet
from alien1 import Alien1
from tools import Tools
from game_states import GameSate
from butten import Button
A=[0,1,2]

class AlienInvasion:
    def __init__(self):#初始化游戏并创建游戏资源
        pygame.init()
        self.clock=pygame.time.Clock()#控制帧率
        self.settings=Settings()#将Settings导入到self.settings
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#注意两个括号
        pygame.display.set_caption("外星人入侵")#屏幕命名
        self.states=GameSate(self)#将Gamestate导入到self.game_state
        self.ship=Ship(self)#将Ship导入到self.ship
        self.bullets=pygame.sprite.Group()#为子弹创建列表
        self.aliens=pygame.sprite.Group()#为外星人创建列表
        self.tools=pygame.sprite.Group()#为道具创建列表
        self._create_fleet()#
        self._create_tools()#
        self.active=False#启动游戏标识
        self.play_button=Button(self,"PLAY")#创建按钮
        self.act=True#贯穿标识

#check事件区
    def _check_events(self):#相应按键与鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#点右上角叉号退出游戏
                sys.exit()
            elif event.type==pygame.KEYDOWN:#按下
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:#松开
                self._check_keyup_event(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.active:
            self.states.reset_stats()
            self.active=True
            #清空外星人
            self.aliens.empty()
            self.ship.center_ship()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        self.settings.fleet_direction*=-1

    def _check_bullet_alien_collisions(self):
        #如果有子弹击中外星人
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,self.act,True)
        #如果没有外星人就再来
        if not self.aliens:
            self.act=True
            self.bullets.empty()
            self.tools.empty()
            self.settings.bullet_color=(0,0,0)
            self.settings.ship_speed=5
            self._create_tools()
            self._create_fleet()

    def _check_tool_ship_collisions(self):
        #如果飞船击中道具
        if pygame.sprite.spritecollideany(self.ship,self.tools):
            self.act=False
            self.settings.bullet_color=(255,0,0)
            self.settings.ship_speed=10
            self.tools.empty()

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.settings.screen_height:
                #像被飞船装了
                self._ship_hit()
                break


    def _ship_hit(self):
        if self.states.ship_left>0:
            self.states.ship_left-=1
            print(f"飞船还有{self.states.ship_left}命")
            #清空外星人列表
            self.aliens.empty()
            #将飞船放在底部中央
            self.ship.center_ship()
            #暂停一会
            ruo=pygame.mixer.Sound(os.path.join("voice/弱耶.mp3"))
            sila=pygame.mixer.Sound(os.path.join("voice/死啦.mp3"))
            meihui=pygame.mixer.Sound(os.path.join("voice/每回.mp3"))
            if random.choice(A)==1:
                ruo.set_volume(2)
                ruo.play()
                time.sleep(3)
            elif random.choice(A)==0:
                sila.set_volume(2)
                sila.play()
                time.sleep(2)
            else:
                meihui.set_volume(2)
                meihui.play()
                time.sleep(2)
        else:
            self.active=False
             
                                

    def _check_keydown_events(self,event):#按下
        if event.key==pygame.K_d:
            self.ship.moving_right=True
        if event.key==pygame.K_a:
            self.ship.moving_left=True
        if event.key==pygame.K_w:
            self.ship.moving_up=True
        if event.key==pygame.K_s:
            self.ship.moving_down=True
        if event.key==pygame.K_j:
            self._fire_bullet()
            woo=pygame.mixer.Sound(os.path.join("voice/Woo.mp3"))
            woo.play()
            self.ship.image=pygame.image.load("image/state(2).png")
        if event.key==pygame.K_ESCAPE:
            sys.exit()
        
    def _check_keyup_event(self,event):#松开
        if event.key==pygame.K_d:
            self.ship.moving_right=False
        if event.key==pygame.K_a:
            self.ship.moving_left=False
        if event.key==pygame.K_w:
            self.ship.moving_up=False
        if event.key==pygame.K_s:
            self.ship.moving_down=False
        if event.key==pygame.K_j:
            self.ship.image=pygame.image.load("image/state(1).png")

#创造区
    def _fire_bullet(self):
        #创建一颗子弹并加入列表中
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        #创建一个起始外星人
        alien=Alien1(self)
        self.aliens.add(alien)
        #外星人之间间距为一个外星人宽
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height#current_x表示下一个外星人的水平位置
        while current_y<(self.settings.screen_height-7*alien_height):
            while current_x<(self.settings.screen_width-2*alien_width):
                if random.choice(A)==1:
                    self._create_alien(current_x,current_y)
                current_x+=2*alien_width#单行内不断累加
            #下一行重置x递增y
            current_x=alien_width
            current_y+=2*alien_height

    def _create_alien(self,x_position,y_position):
        #创建一个新外星人
        new_alien=Alien1(self)
        new_alien.x=x_position
        new_alien.y=y_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
    
    def _create_tools(self):
        tool=Tools(self)
        self.tools.add(tool)




#刷新区
    def _update_screen(self):#刷新屏幕
        self.screen.blit(self.settings.background_image,(0,0))#绘制图片
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()#绘制飞船
        self.aliens.draw(self.screen)#绘制外星人
        self.tools.draw(self.screen)#绘制道具
        if not self.active:
            self.play_button.draw_button()
        pygame.display.flip()#让最近绘制的屏幕可见

    def _update_bullets(self):#刷新子弹
        self.bullets.update()#更新子弹位置
        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
                                    
    def _update_aliens(self):#刷新外星人
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):#不是group的放前面
        #检测外星人是否与飞船碰撞
            self._ship_hit()
        #检测是否有外星人到达了屏幕下边缘
        self._check_aliens_bottom()

    def _update_tools(self):#刷新道具       
        self.tools.update()
        self._check_tool_ship_collisions()
        

#开始游戏
    def run_game(self):#开始游戏循环
        nggyu=pygame.mixer.Sound(os.path.join("voice/NGGYU.mp3"))
        nggyu.set_volume(0.5)
        nggyu.play()
        while True:
            self._check_events()#相应按键与鼠标事件
            if self.active:
                self.ship.update()#更新飞船位置
                self._update_bullets()#刷新子弹
                self._update_tools()#刷新道具
                self._update_aliens()#刷新外星人
            self._update_screen()#刷新屏幕
            self.clock.tick(60)#帧率为60

if __name__=="__main__":#创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()
