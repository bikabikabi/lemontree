import random
import threading
import time
import pygame
from .model import DataBuffer
from .utils import pop_window


# 工具类
class VisualTool:
    def __init__(self, sort_fun, data=None, interval=0.1):
        pygame.init()  # 初始化pygame
        
        self.sort_fun = sort_fun  # 排序函数
        self.interval = interval  # 间隔
        self.screen = pygame.display.set_mode((1920 * 0.8, 1080 * 0.8))  # 设置屏幕
        
        if data:
            self.data = DataBuffer(data, self.screen)  # 如果有数据则使用给定数据
        else:
            self.random_init(1, 30)  # 否则随机生成1-30的数据
        
        self.clock = pygame.time.Clock()  # 时钟
        self.over = False  # 是否结束
    
    # 结束
    def kill(self):
        self.over = True
        pygame.quit()
    
    # 加载txt文件
    def load_txt(self, path):
        self.load(path)
    
    # 加载csv文件
    def load_csv(self, path):
        self.load(path, ',')
    
    # 加载文件
    def load(self, path, Separator=' '):
        try:
            # 打开文件
            with open(path, 'rt', encoding="utf_8") as f:
                data = f.readline()  # 读取一行
            
            data = list(map(int, data.split(Separator)))
            # 分割字符串转换为整数
            self.data = DataBuffer(data, self.screen)
            # 创建数据缓存
        
        except Exception as E:
            print(E)  # 捕获异常
    
    # 随机生成数据
    def random_init(self, a, b=None):
        if b:
            data = list(range(a, b))  # a到b之间的随机数据
        else:
            data = list(range(a))  # 0到a之间的随机数据
        
        random.shuffle(data)  # 随机乱序
        self.data = DataBuffer(data, self.screen)  # 创建数据缓存
    
    # 获取数据
    def get_data(self):
        return self.data.data
    
    # 运行排序函数
    def run_sort_fun(self):
        try:
            self.sort_fun(self.get_data(), self.select_two, self.select_one, self.swap, self.lock)
        
        except Exception as E:
            print(E)  # 捕获异常
    
    # 运行工具
    def run(self):
        # 创建线程运行排序函数
        t = threading.Thread(target=self.run_sort_fun)
        
        t.daemon = True
        t.start()
        # 事件循环
        while True:
            self.clock.tick(30)  # 每秒30帧
            
            for event in pygame.event.get():  # 事件循环
                if event.type == pygame.QUIT:  # 如果点击关闭窗口
                    self.kill()  # 结束
                    pygame.quit()  # 退出pygame
                    return
            
            self.draw()  # 绘制
            pygame.display.flip()  # 刷新屏幕
    
    # 绘制
    def draw(self):
        self.screen.fill(pygame.Color('black'), self.screen.get_rect())
        # 填充黑色
        self.data.draw()  # 绘制数据
    
    # 选中两个数字
    def select_two(self, i, j, color1="red", color2="red"):
        
        if not self.over:  # 如果没有结束
            self.data.select_two_group_members_ids(i, j, color1, color2)
            # 选中两个数字
            time.sleep(self.interval)  # 间隔
        else:
            raise Exception("中断")  # 如果结束则抛出中断异常
    
    # 选中一个数字
    def select_one(self, index):
        self.data.select_group_member(index)
        # 选中一个数字
    
    # 锁定数字
    def lock(self, index):
        self.data.lock(index)
        # 锁定数字
    
    # 交换两个数字
    def swap(self, i, j):
        self.data.swap(i, j)  # 交换两个数字
        time.sleep(self.interval)  # 间隔


# 动画启动器
def start_animation(sort, path, interval, maxvalue):
    try:
        
        # 类型转换失败说明数据格式不对
        interval = float(interval)  # 间隔转换为浮点数
        maxvalue = int(maxvalue)  # 数据规模转换为整数
    
    except Exception as E:
        # 弹出错误窗口
        pop_window("元运算间隔(数字)或数据规模(整数)错误")
        print(E)
        return E
    
    if path:
        # 如果有文件路径
        if path.split(".")[-1] == "csv":  # 如果是csv文件
            tool = VisualTool(sort)  # 创建工具
            tool.load_csv(path)  # 加载csv文件
        elif path.split(".")[-1] == "txt":  # 如果是txt文件
            tool = VisualTool(sort)  # 创建工具
            tool.load_txt(path)  # 加载txt文件
        else:
            pop_window("文件路径错误")  # 弹出文件路径错误窗口
            return
    else:
        # 没有文件路径
        tool = VisualTool(sort)  # 创建工具
        if maxvalue:
            # 如果有数据规模
            tool.random_init(1, maxvalue)  # 随机生成1到maxvalue的数据
    if interval:
        # 如果有间隔
        tool.interval = interval  # 设置间隔
    tool.run()  # 运行
