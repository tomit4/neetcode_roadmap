class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def find_max(root: TreeNode | None) -> int | float:
    if not root:
        return float("-inf")  # Return negative infinity if tree is empty

    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.value, left_max, right_max)


max_value = find_max(root)
print("max_value :=> ", max_value)
assert max_value == 5
