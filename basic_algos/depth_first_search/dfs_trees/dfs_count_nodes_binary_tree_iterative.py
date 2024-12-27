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

    stack = [root]
    count = 0

    while stack:
        node = stack.pop()
        count += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return count


total_nodes = count_nodes(root)
print("total_nodes :=> ", total_nodes)
assert total_nodes == 5
