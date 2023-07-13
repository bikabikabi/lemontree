import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()

        self.image = pygame.image.load(r'img/bullet.png')
        self.rect = self.image.get_rect()
        self.speed = 2

        # 设置初始位置在屏幕顶部
        self.rect.centerx = x
        self.rect.top = y

    def update(self):

        self.rect.top -= self.speed

        # 如果飞机移出屏幕底端,销毁对象
        if self.rect.bottom <0:
            self.kill()
