# 冒泡排序
def bubble_sort(data, select_two, select_one, swap, lock):
    
    for i in range(len(data)):
        # 遍历数组
        for j in range(len(data) - i - 1):
            # 遍历下标大于i的数
            select_two(j, j + 1)  # 选中两个数字
            if data[j] > data[j + 1]:
                # 如果第一个数大于第二个数
                swap(j, j + 1)  # 交换两个数
        lock(len(data) - i - 1)  # 锁定已排序的数


# 选择排序
def select_sort(data, select_two, select_one, swap, lock):
    
    for i in range(len(data)):
        # 遍历数组
        min_index = i  # 最小数下标
        for j in range(i + 1, len(data)):
            # 遍历i之后的数
            select_two(j, min_index)  # 选中两个数字
            if data[j] < data[min_index]:
                # 如果找到比最小数更小的数
                min_index = j  # 更新最小数下标
        swap(i, min_index)  # 交换两个数
        lock(i)  # 锁定已排序的数


# 插入排序
def insert_sort(data, select_two, select_one, swap, lock):
    
    for i in range(len(data)):
        # 遍历数组
        for j in range(i).__reversed__():
            # 逆序遍历i之前的数
            select_two(j, j + 1, color2="yellow")  # 选中两个数,第二个是黄色
            if data[j + 1] < data[j]:
                # 如果后一个数小于前一个数
                swap(j, j + 1)  # 交换两个数
            else:
                # 否则跳出循环
                break
    for i in range(len(data)):
        # 遍历数组
        lock(i)  # 锁定已排序的数


# 快速排序
def quick_sort(data, select_two, select_one, swap, lock):
    
    def sort(left, right):
        # 快速排序函数
        if left < right:
            # 如果左下标小于右下标
            pivot = partition(left, right)  # 分区操作
            sort(left, pivot - 1)  # 对左部分递归调用
            sort(pivot + 1, right)  # 对右部分递归调用
        elif left == right:
            # 如果左下标等于右下标
            lock(left)  # 锁定
            lock(right)  # 锁定
    
    def partition(left, right):
        # 划分操作
        pivot = left  # 选取最左值为pivot
        select_one(pivot)  # 选中pivot
        i = left + 1  # 右指针
        j = right  # 左指针
        while True:  # 循环
            while i <= j and data[i] <= data[pivot]:
                # 右指针向右移动,直到大于pivot
                select_two(i, j)
                i += 1
            while i <= j and data[j] > data[pivot]:
                # 左指针向左移动,直到小于等于pivot
                select_two(i, j)
                j -= 1
            if i > j:
                # 如果指针交叉,跳出循环
                break
            swap(i, j)  # 交换左右指针指向的元素
        swap(pivot, j)  # 将pivot与左指针交换
        lock(j)  # 锁定pivot所在位置
        return j  # 返回pivot的位置


# 希尔排序
def shell_sort(data, select_two, select_one, swap, lock):
    
    gap = len(data) // 2  # 初始步长
    while gap > 0:
        for i in range(gap, len(data)):
            # 遍历不小于步长的元素
            j = i
            
            # 插入排序
            while j >= gap and data[j - gap] > data[j]:
                select_two(j - gap, j, color2='yellow')  # 选中两个数,第二个是黄色
                swap(j - gap, j)  # 交换两个数
                j -= gap  # 后移
                
        gap //= 2  # 更新步长
    for i in range(len(data)):
        # 遍历数组
        lock(i)  # 锁定已排序的数
