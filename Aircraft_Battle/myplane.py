import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.img = pygame.image.load(r'img/myplane.png')
        self.rect = self.img.get_rect()
        self.rect.y = screen_height
        self.rect.centerx = screen_width / 2
        self.speed = 5
        self.d_x = 0
        self.d_y = 0

    def move(self):
        self.rect.y += self.speed * self.d_y
        self.rect.x += self.speed * self.d_x

    def update(self):
        self.move()
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height

        if self.rect.centerx <= 0:
            self.rect.centerx = 0
        elif self.rect.centerx >= self.screen_width:
            self.rect.centerx = self.screen_width
