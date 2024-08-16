import pygame.font
from pathlib import Path
import json

class ScoreBoard:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.states
        #显示得分时字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #准备初始化得分图像
        self.prep_score()
        #
        self.prep_high_score()

    def prep_high_score(self):
        #三位打个逗号
        high_score_str=f"High Score:{self.stats.high_score:,}"
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        #将得分显示在屏幕左上角
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.left=self.screen_rect.left
        self.high_score_rect.top=self.score_rect.top

    def prep_score(self):
        #三位打个逗号
        score_str=f"{self.stats.score:,}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        #将得分放再屏幕右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right
        self.score_rect.top=0

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        path=Path("high_score.json")#将历史最高分存入json
        A={"high_score":self.stats.high_score}
        path.write_text(json.dumps(A))

    def _check_high_score(self):
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()