import pygame
import random

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 时钟
clock = pygame.time.Clock()

# 技能类
class Skill:
    def __init__(self, name, cool_down, effect):
        self.name = name
        self.cool_down = cool_down
        self.effect = effect
        self.last_used = 0
        self.is_available = True

    def use(self):
        if self.is_available:
            self.is_available = False
            self.last_used = pygame.time.get_ticks()
            print(f"使用技能: {self.name}, 效果: {self.effect}")

    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.is_available and current_time - self.last_used >= self.cool_down:
            self.is_available = True

# 定义技能
skills = [
    Skill("火球术", 5000, "造成范围伤害"),
    Skill("治疗术", 8000, "恢复生命值"),
    Skill("闪电链", 3000, "连锁攻击多个敌人")
]

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 检测按键使用技能
    keys_pressed = pygame.key.get_pressed()
    for skill in skills:
        if keys_pressed[ord(skill.name[0])] and skill.is_available:
            skill.use()

    # 更新技能状态
    for skill in skills:
        skill.update()

    # 绘制界面
    screen.fill(BLACK)
    y = 50
    for skill in skills:
        pygame.draw.rect(screen, GREEN if skill.is_available else RED, (50, y, 200, 30))
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"{skill.name}: {'可用' if skill.is_available else '冷却中'}", True, WHITE)
        screen.blit(text, (50, y))
        y += 50

    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出程序
pygame.quit()