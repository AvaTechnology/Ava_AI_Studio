import pygame
import random
import math

# 窗口大小
WIDTH = 600
HEIGHT = 600

# 粒子颜色
COLORS = [(255, 0, 255), (255, 192, 203), (255, 255, 0)]


def draw_particles(surface, color, num_particles, center_x, center_y, radius):
    for _ in range(num_particles):
        # 根据距离中心的远近计算粒子的密度
        t = random.uniform(0, 2 * math.pi)
        u = random.uniform(0, 1) + random.uniform(0, 1)
        if u > 1:
            r = 2 - u
        else:
            r = u
        x = int(center_x + radius * r * math.cos(t))
        y = int(center_y - radius * r * math.sin(t))

        # 绘制粒子
        pygame.draw.circle(surface, color, (x, y), 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Heart Particles")

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))  # 清空屏幕

        # 绘制第一个心形
        center_x = WIDTH // 2 - 120
        center_y = HEIGHT // 2 - 50
        radius = 200

        for i, color in enumerate(COLORS):
            num_particles = int(1000 - 700 * i / (len(COLORS) - 1))
            draw_particles(screen, color, num_particles, center_x, center_y, radius)

        # 绘制第二个心形
        center_x = WIDTH // 2 + 120
        center_y = HEIGHT // 2 - 50
        radius = 200

        for i, color in enumerate(COLORS):
            num_particles = int(1000 - 700 * i / (len(COLORS) - 1))
            draw_particles(screen, color, num_particles, center_x, center_y, radius)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()
