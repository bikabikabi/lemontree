import tkinter as tk
from tkinter import filedialog


def set_func(call, fun):
    # 设置函数
    # 闭包
    return lambda path, interval, maxvalue: call(fun, path=path, interval=interval, maxvalue=maxvalue)


# 菜单类
class menu:
    
    def __init__(self, title, items, font=('黑体', 10, 'bold')):
        
        self.items = self.create_call_list(items)  # 创建调用列表
        self.font = font  # 字体
        self.title = title  # 标题
        self.fun_dic = {}  # 函数字典
        self.size = self.get_size()  # 获取窗口大小
        
        self.window = tk.Tk()  # 创建窗口
        self.window.title(title)  # 设置标题
        self.window.geometry(str(self.size[0]) + 'x' + str(self.size[1]))
        # 设置大小
        
        self.window.columnconfigure(0, weight=1)  # 列权重
        self.window.columnconfigure(1, weight=3)
        
        self.left = tk.Frame(self.window)  # 左框架
        self.left.grid(row=1, column=0, sticky="WE")
        
        self.right = tk.Frame(self.window)  # 右框架
        self.right.columnconfigure(0, weight=1)  # 列权重
        self.right.columnconfigure(1, weight=3)
        self.right.columnconfigure(2, weight=1)
        self.right.grid(row=1, column=1, sticky="WE")
        
        # 文件路径
        self.path = tk.StringVar()
        # 文件路径输入框
        self.path_entry = tk.Entry(self.right, textvariable=self.path, font=('黑体', 10), width=30)
        # 选择文件路径按钮
        self.path_button = tk.Button(self.right, text='选择路径', command=self.get_path)
        
        # 间隔
        self.interval = tk.IntVar()
        # 间隔输入框
        self.interval_entry = tk.Entry(self.right, textvariable=self.interval, font=('黑体', 10), width=30)
        
        # 数据规模
        self.maxvalue = tk.IntVar()
        # 数据规模输入框
        self.maxvalue_entry = tk.Entry(self.right, textvariable=self.maxvalue, font=('黑体', 10), width=30)
        
        # 重置按钮
        self.reset_button = tk.Button(self.right, text="重置", command=self.reset)
        
        # 组件初始化
        self.init()
    
    # 创建调用列表
    # 闭包
    def create_call_list(self, items):
        def fun(call):
            return lambda: call(self.path_entry.get(), self.interval_entry.get(), self.maxvalue_entry.get())
        
        result = []
        for item in items:
            result.append([item[0], fun(item[1])])  # 添加调用列表项目
        
        return result
    
    # 初始化
    def init(self):
        # 标题标签
        label = tk.Label(self.window,
                         text='可视化排序算法',
                         font=('黑体', 40, 'bold'),
                         fg='#2c3e50', bg='#f1c40f',
                         height=2,
                         relief='raised', bd=5
                         )
        label.grid(row=0, column=0, columnspan=2, sticky="WE")
        
        for item in self.items:
            # 添加项目
            self.create_item(*item)
        
        label = self.create_label(self.right, '文件路径')  # 文件路径标签
        label.grid(row=0, column=0, sticky="WE")
        self.path_entry.grid(row=0, column=1, sticky="WE")  # 文件路径输入框
        self.path_button.grid(row=0, column=2, )  # 选择文件路径按钮
        
        label = self.create_label(self.right, '元运算间隔')  # 间隔标签
        label.grid(row=1, column=0, sticky="WE")
        self.interval_entry.grid(row=1, column=1, sticky="WE")  # 间隔输入框
        label = self.create_label(self.right, "秒")  # 秒标签
        label.grid(row=1, column=2, sticky="WE")
        
        label = self.create_label(self.right, '数据规模')  # 数据规模标签
        label.grid(row=2, column=0, sticky="WE")
        self.maxvalue_entry.grid(row=2, column=1, sticky="WE")  # 数据规模输入框
        label = self.create_label(self.right, '1-n')  # 1-n标签
        label.grid(row=2, column=2, sticky="WE")
        
        self.reset_button.grid(row=3, column=1, sticky="WE")  # 重置按钮
    
    # 创建标签
    def create_label(self, root, text):
        return tk.Label(root,
                        text=text,
                        font=self.font,
                        fg='#2c3e50',
                        height=2,
                        )
    
    # 重置
    def reset(self):
        self.interval.set(0)
        self.path.set('')
        self.maxvalue.set(0)
    
    # 获取文件路径
    def get_path(self):
        path = filedialog.askopenfilename(title='请选择文件')
        self.path.set(path)
    
    # 获取窗口大小
    def get_size(self):
        n = len(self.items)
        h = 130 + n * 50
        w = 700
        
        # 高度最少500
        h = max(h, 500)
        
        return w, h
    
    # 运行窗口
    def run(self):
        self.window.mainloop()
    
    # 魔术方法()
    def __call__(self):
        self.run()
    
    # 创建项目
    def create_item(self, name, call=None, bg='green', ):
        b = tk.Button(self.left,
                      text=name,  # 文本
                      bg=bg, fg='#fff',  # 背景颜色和字体颜色
                      font=self.font,  # 字体
                      height=2,
                      relief='raised', bd=10,  # 按键效果
                      activebackground='#f1c40f',  # 被按下的背景颜色
                      command=call  # 命令
                      )
        
        self.fun_dic[name] = call  # 添加到函数字典
        b.pack(fill='x')
