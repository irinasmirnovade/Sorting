
class QuickSort:

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