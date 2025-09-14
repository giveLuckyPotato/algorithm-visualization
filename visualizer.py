import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import numpy as np

class SortingVisualizer:
    def __init__(self, arr, title="Sorting Visualization"):
        self.arr = arr[:]
        self.origial_arr = arr[:]
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.title = title
        self.bar_rects = self.ax.bar(np.arange(len(arr)), arr, align="edge", color='skyblue')
        self.ax.set_xlim(0, len(arr))
        self.ax.set_ylim(0, int(1.1 * max(arr)))
        self.ax.set_title(title)
        plt.subplots_adjust(bottom=0.2) # 给按钮留空间

    def update(self, arr, idx1=None, idx2=None):
        """更新柱状图"""
        for rect, val in zip(self.bar_rects, arr):
            rect.set_height(val)
        # 高亮正在操作的柱子
        for i, rect in enumerate(self.bar_rects):
            if i == idx1 or i == idx2:
                rect.set_color('red')
            else:
                rect.set_color('skyblue')
        self.fig.canvas.draw()
        plt.pause(0.01) # 必须加这个才能实时刷新

    def show(self):
        plt.show()

    def reset(self):
        """重置数据"""
        self.arr = self.original_arr[:]
        self.update(self.arr)
