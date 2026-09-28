from bubble_sort import BubbleSort
from quick_sorting import QuickSort
from quick_sorting_median_of_three import QuickSort_median_of_three
from binary_three_sorting import BinaryTreeSort

from array100 import arr_100
from arr_1000 import arr_1000


#sorter_100 = BubbleSort(arr_100)
#sorter_100 = QuickSort(arr_100)
#sorter_100 = QuickSort_median_of_three(arr_100)
sorter_100 = BinaryTreeSort(arr_100)
sorter_100.sort()
steps_100 = sorter_100.get_steps()
result100 = sorter_100.sort()


#sorter_1000 = BubbleSort(arr_1000)
#sorter_1000 = QuickSort(arr_1000)
#sorter_1000 = QuickSort_median_of_three(arr_1000)
sorter_1000 = BinaryTreeSort(arr_1000)
sorter_1000.sort()
steps_1000 = sorter_1000.get_steps()
result1000 = sorter_1000.sort()

ratio_n = 1000 / 100
ratio_steps = steps_1000 / steps_100

print(result100)
print(f"Steps taken: {steps_100}")
print(f"Time complexity: {sorter_100.get_complexity()}")

print(result1000)
print(f"Steps taken: {steps_1000}")
print(f"Time complexity: {sorter_1000.get_complexity()}")

print("n-Verhältnis:", ratio_n)
print("Steps-Verhältnis:", ratio_steps)
