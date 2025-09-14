import time

def bubble_sort(arr, visualizer=None):
    """冒泡排序"""
    n = len(arr)
    # 大的数往后面冒
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            # 如果传入了 visualizer，就更新画面
            if visualizer:
                visualizer.update(arr, j, j+1) # 高亮正在比较的两个元素
                time.sleep(0.05) # 控制动画速度

def selection_sort(arr, visualizer=None):
    """选择排序"""
    n = len(arr)
    for i in range(n):
        min_dex = i
        for j in range(i+1, n):
            if arr[min_dex] > arr[j]:
                min_dex = j
            if visualizer:
                visualizer.update(arr, j, min_dex)
                time.sleep(0.05)
        arr[i], arr[min_dex] = arr[min_dex], arr[i]
        if visualizer:
            visualizer.update(arr, i, min_dex)
            time.sleep(0.05)

def insertion_sort(arr, visualizer=None):
    """插入排序"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            if visualizer:
                visualizer.update(arr, j, j+1)
                time.sleep(0.05)
            j -= 1
        arr[j+1] = key
        if visualizer:
            visualizer.update(arr, j+1, j)
            time.sleep(0.05)