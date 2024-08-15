import pygame
import time

pygame.init()

# 屏幕设置
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("定时输出示例")

# 时钟对象
clock = pygame.time.Clock()

# 定义输出的时间间隔（以毫秒为单位）
interval = 1000  # 1 秒

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 计算时间间隔
    current_time = time.time()
    if current_time - last_output_time >= interval:
        print("输出值")
        last_output_time = current_time

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

pygame.quit()