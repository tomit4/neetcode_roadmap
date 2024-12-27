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
    total = 0

    def dfs(node: TreeNode | None):
        nonlocal total
        if not node:
            return

        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                return

            total += node.value

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    dfs(root)
    return total


total: int = sum_tree(root)
print("total :=> ", total)
assert total == 28
