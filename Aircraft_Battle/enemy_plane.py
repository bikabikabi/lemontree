import random

import pygame


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(r'img/enemy.png')
        self.rect = self.image.get_rect()
        self.speed = 1

        # 设置初始位置在屏幕顶部
        self.rect.centerx = self.screen_width*random.random()
        self.rect.top = 0

    def update(self):
        # 飞机从上向下移动
        self.rect.top += self.speed

        # 如果飞机移出屏幕底端,销毁对象
        if self.rect.top > self.screen_height:
            self.kill()
