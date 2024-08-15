import pygame
import time

# 初始化 Pygame
pygame.init()

# 屏幕设置
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 时钟
clock = pygame.time.Clock()

# 技能释放标志
skill_released = False

# 技能冷却时间（以秒为单位）
skill_cool_down = 5
last_skill_time = 0  # 上次释放技能的时间

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 检测按键释放技能
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE] and not skill_released and time.time() - last_skill_time >= skill_cool_down:
        skill_released = True
        print("技能释放")
        last_skill_time = time.time()

    # 判断技能是否冷却完毕
    if time.time() - last_skill_time >= skill_cool_down:
        print("技能冷却完毕")

    # 刷新屏幕
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出程序
pygame.quit()