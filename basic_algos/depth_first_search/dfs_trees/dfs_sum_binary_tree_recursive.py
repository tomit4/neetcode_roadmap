class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Create a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


def sum_tree(root: TreeNode | None) -> int:
    if not root:
        return 0

    total = root.value
    total += sum_tree(root.left)
    total += sum_tree(root.right)

    return total


total: int = sum_tree(root)
print("total :=> ", total)
assert total == 28
