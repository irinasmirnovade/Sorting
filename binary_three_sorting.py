

class BinaryTreeSort:

    def __init__(self, data):
        self.data = data
        self.steps = 0

    def sort(self):

        self.steps = 0

        # Create the root of the binary tree
        root = None

        # Insert all elements into the binary search tree
        for value in self.data:
            root = self.insert(root, value)

        # Get the elements in sorted order
        result = []
        self.inorder(root, result)

        return result

    def insert(self, node, value):

        self.steps += 1

        # If the place is empty — create a new node
        if node is None:
            return {
                "value": value,
                "left": None,
                "right": None
            }

        # Smaller value goes to the left subtree
        if value < node["value"]:
            node["left"] = self.insert(node["left"], value)

        # Larger or equal — to the right subtree
        else:
            node["right"] = self.insert(node["right"], value)

        return node

    def inorder(self, node, result):

        if node is not None:

            # Visit the left subtree first
            self.inorder(node["left"], result)

            # Then add the current value
            result.append(node["value"])

            # Visit the right subtree
            self.inorder(node["right"], result)

    def get_steps(self):
        return self.steps

    def get_complexity(self):
        return "Average: O(n log n), Worst: O(n²)"