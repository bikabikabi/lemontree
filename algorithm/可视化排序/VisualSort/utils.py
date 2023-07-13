import tkinter as tk


# 获取初始参数
def get_initial_params(data, width, height):
    num = len(data)  # 数字数量
    max_value = max(data)  # 最大值
    result = []
    r_width = width / num  # 宽度比例
    
    for i, value in enumerate(data):
        r_height = (value / max_value) * height  # 高度比例
        x = r_width * i  # x坐标
        y = height - r_height  # y坐标
        result.append((value, x, y, r_width, r_height))  # 添加参数
    
    return result


# 弹出窗口
def pop_window(info):
    window = tk.Toplevel()
    window.wm_title("提示")  # 设置窗口标题
    
    w = 300  # 窗口宽度
    h = 200  # 窗口高度
    sw = window.winfo_screenwidth()  # 屏幕宽度
    sh = window.winfo_screenheight()  # 屏幕高度
    x = (sw - w) / 2  # x坐标
    y = (sh - h) / 2  # y坐标
    
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # 设置窗口大小和位置
    
    tk.Label(window, text=info, font=('黑体', 20, 'bold'), wrap=280).pack()
    # 添加文字
    
    window.after(3000, window.destroy)  # 3秒后销毁窗口
