import random

from algorithms import bubble_sort, selection_sort, insertion_sort
from visualizer import SortingVisualizer

def generate_data(size=20, reverse=False, sorted=False):
    """生成测试数据"""
    if sorted:
        return list(range(1, size+1))
    elif reverse:
        return list(range(size, 0, -1))
    else:
        data = list(range(1, size+1))
        random.shuffle(data)
        return data

def main():
    print("===排序算法可视化实验室===")
    print("1. 冒泡排序")
    print("2. 选择排序")
    print("3. 插入排序")
    choice = input("请选择算法（1-3）：").strip()

    size = int(input("请选择数据规模（建议10-50）: ") or 20)
    data = generate_data(size, reverse=False)

    algo_map = {
        '1': ("bubble sort", bubble_sort),
        '2': ("selection sort", selection_sort),
        '3': ("insertion sort", insertion_sort),
    }

    if choice not in algo_map:
        print("无效选择")
        return

    algo_name, algo_func = algo_map[choice]
    print(f"正在执行 {algo_name}.....")
    visualizer = SortingVisualizer(data, title=algo_name)
    algo_func(data, visualizer=visualizer)
    visualizer.show()

if __name__ == "__main__":
    main()