class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_tree(root: TreeNode | None) -> int:
    total = 0

    def dfs(node: TreeNode | None):
        nonlocal total
        if not node:
            return

        total += node.value
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return total
