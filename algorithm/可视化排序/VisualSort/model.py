import pygame
from pygame.sprite import Sprite
from .utils import get_initial_params


# 数字类
class Number(Sprite):
    def __init__(self, value, x, y, width, height):
        super().__init__()
        self.width = width  # 宽度
        self.height = height  # 高度
        self.value = value  # 数值
        self.image = pygame.Surface((width, height))  # 创建surface
        self.image.fill(pygame.Color('white'))  # 填充白色
        pygame.draw.rect(self.image, pygame.Color('black'), (0, 0, width, height), 1)
        # 画黑色边框
        self.rect = self.image.get_rect()  # 获取rect
        self.rect.x = x  # 设置x坐标
        self.rect.y = y  # 设置y坐标
        self.locked = False  # 是否锁定
    
    # 选中效果
    def checked(self, color):
        # 如果没有锁定
        if not self.locked:
            self.image.fill(pygame.Color(color))  # 填充选中颜色
            pygame.draw.rect(self.image, pygame.Color('black'), (0, 0, self.width, self.height), 1)
            # 画黑色边框
    
    # 取消选中效果
    def unchecked(self):
        if not self.locked:
            self.image.fill(pygame.Color('white'))  # 填充白色
            pygame.draw.rect(self.image, pygame.Color('black'), (0, 0, self.width, self.height), 1)
            # 画黑色边框
    
    # 锁定
    def lock(self):
        self.locked = True
        self.image.fill(pygame.Color('blue'))  # 填充蓝色
        pygame.draw.rect(self.image, pygame.Color('black'), (0, 0, self.width, self.height), 1)
        # 画黑色边框
    
    # 大于比较
    def __gt__(self, other):
        return self.value > other.value
    
    # 大于等于比较
    def __ge__(self, other):
        return self.value >= other.value
    
    # 小于比较
    def __lt__(self, other):
        return self.value < other.value
    
    # 小于等于比较
    def __le__(self, other):
        return self.value <= other.value
    
    # 不等比较
    def __ne__(self, other):
        return self.value != other.value


# 数据缓存类
class DataBuffer:
    def __init__(self, data, screen):
        self.screen = screen  # 屏幕
        self.group = pygame.sprite.Group()  # 精灵组
        self.data = []  # 数字列表
        
        width = screen.get_rect().width  # 屏幕宽度
        height = screen.get_rect().height  # 屏幕高度
        initial_params = get_initial_params(data, width, height)
        
        # 获取初始参数
        for i in initial_params:
            number = Number(*i)  # 创建数字
            self.group.add(number)  # 添加到精灵组
            self.data.append(number)  # 添加到数字列表
        
        self.i = -1  # 第一个选中数字
        self.j = -1  # 第二个选中数字
        self.k = -1  # 当前选中的数字
    
    # 选中当前精灵组中的精灵
    def select_group_member(self, index):
        
        if self.k >= 0:
            self.data[self.k].unchecked()  # 取消之前选中的数字选中效果
        self.k = index  # 设置当前选中数字
        self.data[self.k].checked("green")  # 选中当前数字
    
    def select_two_group_members_ids(self, i, j, color1="red", color2="red"):
        
        # 选中两个数字
        if self.i >= 0:
            self.data[self.i].unchecked()  # 取消之前第一个选中数字的选中效果
        if self.j >= 0:
            self.data[self.j].unchecked()  # 取消之前第二个选中数字的选中效果
        self.i = i  # 设置第一个选中数字
        self.j = j  # 设置第二个选中数字
        self.data[self.i].checked(color1)  # 选中第一个数字
        self.data[self.j].checked(color2)  # 选中第二个数字
    
    # 锁定数字
    def lock(self, index):
        
        self.data[index].lock()  # 锁定数字
    
    # 交换两个数字
    def swap(self, i, j):
        
        self.data[i].rect.x, self.data[j].rect.x = self.data[j].rect.x, self.data[i].rect.x
        # 交换x坐标
        self.data[i], self.data[j] = self.data[j], self.data[i]
        # 交换数字
    
    # 绘制
    def draw(self, ):
        
        self.group.draw(self.screen)  # 绘制精灵组
