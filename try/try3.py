import pygame


# 初始化 Pygame 
pygame.init()

# 屏幕大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("跳跃示例")

# 时钟
clock = pygame.time.Clock()

# 玩家类
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.jump_speed = -10
        self.gravity = 1

    def update(self):
        # 应用重力
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # 限制在屏幕内
        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.velocity_y = 0

    def jump(self):
        if self.y == SCREEN_HEIGHT:
            self.velocity_y = self.jump_speed

# 创建玩家对象
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        player.jump()

    player.update()

    # 绘制背景
    screen.fill(BLACK)

    # 绘制玩家
    pygame.draw.rect(screen, WHITE, (player.x, player.y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

# 退出程序
pygame.quit()