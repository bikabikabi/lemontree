from gui import menu, set_func
from VisualSort import start_animation
from VisualSort import functional

# 排序字典
sort_dict = {
    '冒泡排序': set_func(start_animation, functional.bubble_sort),
    # 将start_animation和冒泡排序函数封装
    '选择排序': set_func(start_animation, functional.select_sort),
    # 将start_animation和选择排序函数封装
    '插入排序': set_func(start_animation, functional.insert_sort),
    # 将start_animation和插入排序函数封装
    '快速排序': set_func(start_animation, functional.quick_sort),
    # 将start_animation和快速排序函数封装
    '希尔排序': set_func(start_animation, functional.shell_sort),
    # 将start_animation和希尔排序函数封装
}
# 程序入口
if __name__ == '__main__':
    # 创建菜单
    app = menu("可视化排序", sort_dict.items())
    # 运行菜单
    app()
