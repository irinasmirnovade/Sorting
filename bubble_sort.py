



class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.steps = 0

    def sort(self):
        n = len(self.array)

        for i in range(n):
            for j in range(0, n - i - 1):

                self.steps += 1

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = \
                        self.array[j + 1], self.array[j]

        return self.array

    def get_steps(self):
        return self.steps

    def get_complexity(self):
        return "O(n²)"


