import sys

import pygame

def homework02():
    '''画一个矩形'''
    '''   
      要求:用矩形画一个10层的高楼
      1. 层高:50
      2. 层宽:逐层递减,最宽(1层)200, 每层减8
      3. 颜色:灰色(190, 190, 190)
    '''
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    for i in range(10):
        rect = pygame.Rect(300+4*i, 500-50*i, 200-8 * i, 50)
        print(rect)
        pygame.draw.rect(screen, (190, 190, 190), rect, 1)
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
homework02()

