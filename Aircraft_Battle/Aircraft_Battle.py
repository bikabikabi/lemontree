import random
import sys
import threading
import time

import pygame
from myplane import MyPlane
from enemy_plane import EnemyPlane
from bullet import Bullet


class Aircraft_Battle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("飞机大战")
        self.bullet_time = 1
        self.enemy_time = 5
        self.screen = pygame.display.set_mode((500, 800))

        self.myplane = MyPlane(self.screen.get_height(), self.screen.get_width())
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont([], 50)

    def start(self):
        t = time.time()
        t1 = time.time()
        self.enemys.empty()
        self.bullets.empty()

        while True:
            self.clock.tick(60)
            if time.time() - t > 2:
                t = time.time()
                self.enemy_time -= 0.01
                if self.enemy_time < 1:
                    self.enemy_time = 1
                for i in range(random.randint(1, 5)):
                    self.enemys.add(EnemyPlane(self.screen.get_height(), self.screen.get_width()))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.myplane.d_x -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.myplane.d_x += 1
                    elif event.key == pygame.K_UP:
                        self.myplane.d_y -= 1
                    elif event.key == pygame.K_DOWN:
                        self.myplane.d_y += 1
                    elif event.key == pygame.K_SPACE:
                        if time.time() - t1 > self.bullet_time:
                            t1 = time.time()
                            self.bullets.add(Bullet(self.myplane.rect.centerx, self.myplane.rect.y))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.myplane.d_x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.myplane.d_x -= 1
                    elif event.key == pygame.K_UP:
                        self.myplane.d_y += 1
                    elif event.key == pygame.K_DOWN:
                        self.myplane.d_y -= 1

            if self.update():
                self.gameover()
                return self.score

    def gameover(self):
        print(self.score)

    def update(self):
        self.myplane.update()
        self.bullets.update()

        result = pygame.sprite.groupcollide(self.bullets, self.enemys, True, True)
        self.score += len(result)

        if pygame.sprite.spritecollideany(self.myplane, self.enemys):
            return True

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.myplane.img, self.myplane.rect)
        text = self.font.render(f"score:{self.score}", True, (255, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.x = 0
        textRect.y = 0
        self.screen.blit(text, textRect)
        self.bullets.draw(self.screen)
        self.enemys.update()
        self.enemys.draw(self.screen)
        pygame.display.flip()
        return False
