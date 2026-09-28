

from bubble_sort import BubbleSort
from quick_sorting import QuickSort
from quick_sorting_median_of_three import QuickSort_median_of_three
from binary_three_sorting import BinaryTreeSort

from array100 import arr_100
from arr_1000 import arr_1000


# All sorting algorithms
sorting_algorithms = [
    BubbleSort,
    QuickSort,
    QuickSort_median_of_three,
    BinaryTreeSort
]


# Arrays to test
arrays = [
    ("100", arr_100),
    ("1000", arr_1000)
]


# Store the results
results = []


# Run every sorting algorithm on every array
for algorithm in sorting_algorithms:

    for array_name, data in arrays:

        sorter = algorithm(data.copy())

        result = sorter.sort()

        steps = sorter.get_steps()

        complexity = sorter.get_complexity()

        results.append({
            "Algorithm": algorithm.__name__,
            "Array": array_name,
            "Steps": steps,
            "Complexity": complexity
        })


# Print results
print("\nSorting results")
print("-" * 80)

print(
    f"{'Algorithm':<30}"
    f"{'Array':<10}"
    f"{'Steps':<15}"
    f"{'Complexity':<25}"
)

print("-" * 80)

for result in results:

    print(
        f"{result['Algorithm']:<30}"
        f"{result['Array']:<10}"
        f"{result['Steps']:<15}"
        f"{result['Complexity']:<25}"
    )