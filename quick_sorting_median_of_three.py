class QuickSort_median_of_three:

    def __init__(self, array):
        self.array = array
        self.steps = 0

    def sort(self):
        self._quick_sort(0, len(self.array) - 1)
        return self.array

    def _quick_sort(self, low, high):

        if low < high:

            pivot_index = self._partition(low, high)

            self._quick_sort(low, pivot_index - 1)
            self._quick_sort(pivot_index + 1, high)

    def _partition(self, low, high):

        # MEDIAN-OF-THREE
        mid = (low + high) // 2

        a = self.array[low]
        b = self.array[mid]
        c = self.array[high]

        if (a <= b <= c) or (c <= b <= a):
            median_index = mid
        elif (b <= a <= c) or (c <= a <= b):
            median_index = low
        else:
            median_index = high

        # ставим выбранный pivot в конец
        self.array[median_index], self.array[high] = \
            self.array[high], self.array[median_index]

        pivot = self.array[high]
 
        i = low - 1

        for j in range(low, high):

            self.steps += 1

            if self.array[j] < pivot:
                i += 1

                self.array[i], self.array[j] = \
                    self.array[j], self.array[i]

        self.array[i + 1], self.array[high] = \
            self.array[high], self.array[i + 1]

        return i + 1

    def get_steps(self):
        return self.steps

    def get_complexity(self):
        return "Average: O(n log n), Worst: O(n²)"