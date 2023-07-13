import random
import sys
import time

import pygame


class game2048:
    data = None
    old_data = None
    over = None
    color = {
        0: (0, 0, 0),
        2: (20, 30, 0),
        4: (40, 20, 90),
        8: (60, 30, 15),
        16: (80, 40, 20),
        32: (100, 50, 25),
        64: (120, 60, 30),
        128: (140, 70, 35),
        256: (160, 10, 40),
        512: (180, 90, 45),
        1024: (70, 100, 50),
        2048: (220, 180, 55),
        
    }
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2048")
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.reset()
    
    def draw(self):
        
        for i in range(4):
            for j in range(4):
                pos = pygame.Rect(i * 100, j * 100, 100, 100)
                color = self.color[self.data[i][j]]
                pygame.draw.rect(self.screen, color, pos, 50)
                if self.data[i][j]!=0:
                    text = self.font.render(str(self.data[i][j]), True, (255, 255, 255))
                    text_rect = text.get_rect(center=pos.center)
                    self.screen.blit(text, text_rect)
        pygame.display.flip()
    
    def get_T(self):
        new_data = []
        for i in range(4):
            new_data.append([])
            for j in range(4):
                new_data[i].append(self.data[j][i])
        self.data = new_data
    
    def show_data(self):
        print("-" * 25)
        for i in self.data:
            print(end="|")
            for j in i:
                print("{:^5}".format(j), end="|")
            
            print('\n', "-" * 25, sep='')
        print()
    
    def merge(self, direction):
        self.zero_to_end(direction)
        reward = -1
        if direction == 0:
            
            for i in range(3):
                for j in range(4):
                    if self.data[i][j] != 0 and self.data[i][j] == self.data[i + 1][j]:
                        reward += 1
                        self.data[i][j] <<= 1
                        self.data[i + 1][j] = 0
        
        elif direction == 1:
            for i in reversed(range(1, 4)):
                for j in range(4):
                    if self.data[i][j] != 0 and self.data[i][j] == self.data[i - 1][j]:
                        reward += 1
                        self.data[i][j] <<= 1
                        self.data[i - 1][j] = 0
        
        elif direction == 2:
            for j in range(3):
                for i in range(4):
                    if self.data[i][j] != 0 and self.data[i][j] == self.data[i][j + 1]:
                        reward += 1
                        self.data[i][j] <<= 1
                        self.data[i][j + 1] = 0
        
        elif direction == 3:
            for j in reversed(range(1, 4)):
                for i in range(4):
                    if self.data[i][j] != 0 and self.data[i][j] == self.data[i][j - 1]:
                        reward += 1
                        self.data[i][j] <<= 1
                        self.data[i][j - 1] = 0
        
        self.zero_to_end(direction)
        return reward
    
    def zero_to_end(self, direction):
        
        if direction == 0:
            self.get_T()
            for i in range(4):
                j = 0
                n = 3
                while j < n:
                    if self.data[i][j] == 0:
                        self.data[i].pop(j)
                        self.data[i].append(0)
                        n -= 1
                        continue
                    j += 1
            self.get_T()
        elif direction == 1:
            self.get_T()
            for i in range(4):
                j = 3
                n = 0
                while j > n:
                    if self.data[i][j] == 0:
                        self.data[i].pop(j)
                        self.data[i].insert(0, 0)
                        n += 1
                        continue
                    j -= 1
            self.get_T()
        elif direction == 2:
            for i in range(4):
                j = 0
                n = 3
                while j < n:
                    if self.data[i][j] == 0:
                        self.data[i].pop(j)
                        self.data[i].append(0)
                        n -= 1
                        continue
                    j += 1
        elif direction == 3:
            for i in range(4):
                j = 3
                n = 0
                while j > n:
                    if self.data[i][j] == 0:
                        self.data[i].pop(j)
                        self.data[i].insert(0, 0)
                        n += 1
                        continue
                    j -= 1
    
    def check(self):
        if self.data[3][3] == 0:
            return False
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == 0 or self.data[i][j] == self.data[i + 1][j] or self.data[i][j] == self.data[i][j + 1]:
                    return False
            if self.data[i][3] == 0 or self.data[i][3] == self.data[i + 1][3]:
                return False
            if self.data[3][i] == 0 or self.data[3][i] == self.data[3][i + 1]:
                return False
        else:
            return True
    
    def reset(self):
        self.data = [[0, 0, 0, 0] for i in range(4)]
        self.old_data = self.data.copy()
        self.random_fill()
        self.random_fill()
        self.over = False
        self.draw()
        return self.data.copy()
    
    def random_fill(self):
        unfilled = [(i, j) for i in range(4) for j in range(4) if self.data[i][j] == 0]
        if unfilled:
            pos = random.choice(unfilled)
            self.data[pos[0]][pos[1]] = random.choice([2, 4])
        else:
            self.over = True
    
    # def is_changed(self):
    #     for i in range(4):
    #         for j in range(4):
    #             if self.data[i][j] != self.old_data[i][j]:
    #                 return True
    #     return False
    
    def step(self, action):
        
        reward = self.merge(action)
        
        self.over = self.check()
        # changed = self.is_changed()
        if self.over:
            reward -= 10
        else:
            self.update()
            self.show_data()
        # return self.data.copy(), reward, self.over, changed
        return self.data.copy(), reward, self.over

    def update(self):
        self.random_fill()
        
        self.draw()
    
    def start(self):
        
        while True:
            self.clock.tick(30)
            
            if self.over:
                self.reset()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.step(0)
                    elif event.key==pygame.K_RIGHT:
                        self.step(1)
                    elif event.key==pygame.K_UP:
                        self.step(2)
                    elif event.key==pygame.K_DOWN:
                        self.step(3)


a = game2048()
a.start()
# a.data = [[0, 2, 2, 0] for i in range(2)]
# a.data.extend([[2, 0, 4, 2] for i in range(2)])
