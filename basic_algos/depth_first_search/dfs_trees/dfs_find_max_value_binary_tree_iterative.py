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
        return float("-inf")

    stack = [root]
    max_value = float("-inf")

    while stack:
        node = stack.pop()
        max_value = max(max_value, node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return max_value


max_value = find_max(root)
print("max_value :=> ", max_value)
assert max_value == 5
