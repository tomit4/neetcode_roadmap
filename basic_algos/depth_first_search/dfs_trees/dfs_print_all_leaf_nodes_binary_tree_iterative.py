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


def print_all_leaf_nodes(root: TreeNode | None):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()

        if not node.left and not node.right:
            print(node.value, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


print("Leaf nodes:", end=" ")
print_all_leaf_nodes(root)
