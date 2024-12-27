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


def count_nodes(root: TreeNode | None) -> int:
    if not root:
        return 0
    total_nodes = 1
    total_nodes += count_nodes(root.left)
    total_nodes += count_nodes(root.right)
    return total_nodes


total_nodes = count_nodes(root)
print("total_nodes :=> ", total_nodes)
assert total_nodes == 5
